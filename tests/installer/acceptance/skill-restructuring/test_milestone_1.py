"""
Milestone 1 Acceptance Tests: Collision-Free Skills.

All scenarios except the first are marked @skip. Enable one at a time
as implementation progresses.

Driving ports: SkillsPlugin.install(), SkillsPlugin.verify()
"""

import pytest
from pytest_bdd import scenario


@scenario(
    "milestone-1-collision-free.feature",
    "All non-colliding skills exist in nw-prefixed directory format",
)
def test_source_structure_nw_prefixed():
    """Source tree has nw-prefixed directories with SKILL.md."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Skill content is preserved after restructuring",
)
def test_content_preserved():
    """File content identical after restructuring."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Skills plugin installs all collision-free skills",
)
def test_install_collision_free():
    """Install 94 non-colliding skills."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Installation reports correct file count",
)
def test_install_reports_count():
    """Installation message includes correct count."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Old namespace directory removed during upgrade installation",
)
def test_upgrade_removes_old_namespace():
    """Upgrade cleans old nw/ directory."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Upgrade replaces all old skills with new layout",
)
def test_upgrade_replaces_layout():
    """Upgrade from old to new layout."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Verification passes when all skills are installed correctly",
)
def test_verify_success():
    """Verification reports success."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Verification detects missing skill directories",
)
def test_verify_detects_missing():
    """Verification catches missing skills."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Agent Skill Loading sections reference new nw-prefixed Read paths",
)
def test_agent_skill_loading_paths():
    """All agent Skill Loading paths use nw-prefixed SKILL.md format."""
    pass


@pytest.mark.skip(reason="Enable after walking skeleton passes")
@scenario(
    "milestone-1-collision-free.feature",
    "Agent definitions no longer contain skill loading workaround",
)
def test_agent_no_workaround():
    """Agent file has no Skill Loading section."""
    pass


@pytest.mark.skip(reason="Enable after walking skeleton passes")
@scenario(
    "milestone-1-collision-free.feature",
    "All public agents are free of skill loading workaround sections",
)
def test_all_agents_no_workaround():
    """All 23 public agents cleaned."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Installation fails gracefully when source directory is missing",
)
def test_error_no_source():
    """Graceful handling of missing source."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Installation handles read-only target directory",
)
def test_error_readonly_target():
    """Permission error handled gracefully."""
    pass


@scenario(
    "milestone-1-collision-free.feature",
    "Verification handles missing target directory",
)
def test_error_no_target():
    """Verification handles missing target."""
    pass
