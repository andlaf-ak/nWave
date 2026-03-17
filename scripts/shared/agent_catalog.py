"""Shared public/private agent filtering logic.

Used by installer plugins and build scripts to exclude private agents
and their skills from public distributions. The source of truth is
``nWave/framework-catalog.yaml`` where each agent has a ``public`` field.

Backward compatibility: when the catalog file is missing or cannot be parsed,
all functions treat every agent as public (empty set semantics).

**Important**: PyYAML must be installed. If missing, ``load_public_agents``
raises ``RuntimeError`` instead of silently returning an empty set (which
would cause all agents to be treated as public — a security leak).
"""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from pathlib import Path


def load_public_agents(nwave_dir: Path) -> set[str]:
    """Read framework-catalog.yaml and return the set of public agent names.

    An agent is public when its ``public`` field is not ``False``.
    Missing ``public`` field defaults to public.

    Returns an empty set when the catalog file is missing or cannot be
    parsed (backward compatibility -- callers treat empty set as
    "include everything").
    """
    catalog_path = nwave_dir / "framework-catalog.yaml"
    if not catalog_path.exists():
        return set()

    try:
        import yaml
    except ModuleNotFoundError:
        msg = (
            "PyYAML is required for agent filtering but is not installed. "
            "Install it with: pip install pyyaml"
        )
        raise RuntimeError(msg) from None

    try:
        with catalog_path.open(encoding="utf-8") as fh:
            catalog = yaml.safe_load(fh)

        return {
            name
            for name, info in catalog.get("agents", {}).items()
            if info.get("public") is not False
        }
    except Exception:
        return set()


def is_public_agent(agent_file_name: str, public_agents: set[str]) -> bool:
    """Check whether an agent file belongs to a public agent.

    Strips the ``nw-`` prefix and ``.md`` suffix to derive the agent name.
    Reviewer agents (``-reviewer`` suffix) inherit the public status of
    their base agent.

    When *public_agents* is empty (catalog not loaded), returns ``True``
    for every file (backward compatibility).
    """
    if not public_agents:
        return True
    agent_name = agent_file_name.removeprefix("nw-").removesuffix(".md")
    base_name = agent_name.removesuffix("-reviewer")
    return agent_name in public_agents or base_name in public_agents


def build_ownership_map(agents_dir: Path) -> dict[str, set[str]]:
    """Build skill-directory-name -> set-of-agent-names mapping from frontmatter.

    Parses each ``nw-*.md`` agent file's YAML frontmatter and extracts
    the ``skills`` list. Returns a dict mapping each skill **directory name**
    (nw-prefixed, as it appears on disk) to the set of agent names that
    reference it.

    Skill keys are nw-prefixed (matching directory names in nWave/skills/).
    Agent values are bare names without nw- prefix (matching public_agents set).

    Example::

        {
            "nw-tdd-methodology": {"software-crafter", "functional-software-crafter"},
            "nw-five-whys-methodology": {"troubleshooter"},
        }
    """
    if not agents_dir.exists():
        return {}

    try:
        import yaml
    except ModuleNotFoundError:
        return {}

    ownership: dict[str, set[str]] = {}

    for agent_file in sorted(agents_dir.glob("nw-*.md")):
        agent_name = agent_file.stem.removeprefix("nw-")
        frontmatter = _parse_frontmatter(agent_file, yaml)
        if frontmatter is None:
            continue
        skills = frontmatter.get("skills")
        if not isinstance(skills, list):
            continue
        for skill in skills:
            # Ensure skill key is nw-prefixed (matches directory name)
            skill_key = skill if skill.startswith("nw-") else f"nw-{skill}"
            ownership.setdefault(skill_key, set()).add(agent_name)

    return ownership


def _parse_frontmatter(file_path: Path, yaml_module: object) -> dict | None:
    """Extract YAML frontmatter from a markdown file.

    Returns the parsed dict, or ``None`` if parsing fails or no
    frontmatter is found.
    """
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError:
        return None

    if not text.startswith("---"):
        return None

    end = text.find("---", 3)
    if end == -1:
        return None

    try:
        return yaml_module.safe_load(text[3:end])  # type: ignore[union-attr]
    except Exception:
        return None


def is_public_skill(
    skill_dir_name: str,
    public_agents: set[str],
    ownership_map: dict[str, set[str]] | None = None,
) -> bool:
    """Check whether a skill directory belongs to a public agent.

    The ``common`` directory is always considered public.
    Reviewer skill directories inherit the public status of their base
    agent.

    When *ownership_map* is provided, uses it to look up the owning
    agent(s) for the skill. A skill is public if at least one of its
    owning agents is public.

    When *ownership_map* is ``None``, falls back to the old heuristic
    (directory name matching).

    When *public_agents* is empty (catalog not loaded), returns ``True``
    for every directory (backward compatibility).
    """
    if not public_agents:
        return True
    if skill_dir_name in ("common", "nw-canary"):
        return True

    if ownership_map is not None:
        # Normalize to nw-prefixed key (matching ownership map convention)
        if skill_dir_name.startswith("nw-"):
            lookup_key = skill_dir_name
        else:
            lookup_key = f"nw-{skill_dir_name}"
        if lookup_key in ownership_map:
            owning_agents = ownership_map[lookup_key]
            return any(agent in public_agents for agent in owning_agents)

    # Fallback: old heuristic (directory name matches agent name)
    base_name = skill_dir_name.removesuffix("-reviewer")
    return skill_dir_name in public_agents or base_name in public_agents
