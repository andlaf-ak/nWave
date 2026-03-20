"""Centralized installation path constants -- single source of truth.

Replaces 10+ scattered hardcoded path constructions across installer
plugins, verifier, and build scripts.

All consumers should import from this module::

    from scripts.shared.install_paths import AGENTS_SUBDIR, agents_dir
"""

from __future__ import annotations

from pathlib import Path


# Relative path segments (appended to claude_dir by callers)
AGENTS_SUBDIR = Path("agents") / "nw"
SKILLS_SUBDIR = Path("skills")
TEMPLATES_SUBDIR = Path("templates")
DES_LIB_SUBDIR = Path("lib") / "python" / "des"
SCRIPTS_SUBDIR = Path("scripts")
COMMANDS_LEGACY_SUBDIR = Path("commands") / "nw"  # deprecated, cleanup only
MANIFEST_FILENAME = "nwave-manifest.txt"


def agents_dir(claude_dir: Path) -> Path:
    """Return the agents installation directory."""
    return claude_dir / AGENTS_SUBDIR


def skills_dir(claude_dir: Path) -> Path:
    """Return the skills installation directory."""
    return claude_dir / SKILLS_SUBDIR


def templates_dir(claude_dir: Path) -> Path:
    """Return the templates installation directory."""
    return claude_dir / TEMPLATES_SUBDIR


def des_dir(claude_dir: Path) -> Path:
    """Return the DES library installation directory."""
    return claude_dir / DES_LIB_SUBDIR


def manifest_path(claude_dir: Path) -> Path:
    """Return the installation manifest file path."""
    return claude_dir / MANIFEST_FILENAME
