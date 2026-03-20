"""
Plugin for cleaning up legacy commands from ~/.claude/commands/nw/.

Commands have been migrated to skill format (nw-*/SKILL.md) as of v2.8.0.
This plugin now only removes the old commands directory during installation
to ensure a clean upgrade path.
"""

import shutil

from scripts.install.plugins.base import (
    InstallationPlugin,
    InstallContext,
    PluginResult,
)


class CommandsPlugin(InstallationPlugin):
    """Plugin for cleaning up legacy commands during upgrade."""

    def __init__(self):
        """Initialize commands plugin with name and priority."""
        super().__init__(name="commands", priority=20)

    def install(self, context: InstallContext) -> PluginResult:
        """Remove legacy commands/nw/ directory if it exists.

        Commands are now installed as skills by the skills plugin.
        This plugin ensures old command files are cleaned up.

        Args:
            context: InstallContext with shared installation utilities

        Returns:
            PluginResult indicating success or failure of cleanup
        """
        try:
            target_commands_dir = context.claude_dir / "commands" / "nw"

            if target_commands_dir.exists():
                count = len(list(target_commands_dir.glob("*.md")))
                shutil.rmtree(target_commands_dir)
                context.logger.info(
                    f"  \U0001f5d1\ufe0f Removed legacy commands/nw/ ({count} files)"
                )

                # Remove parent commands/ if empty
                commands_dir = context.claude_dir / "commands"
                if commands_dir.exists() and not any(commands_dir.iterdir()):
                    commands_dir.rmdir()

                return PluginResult(
                    success=True,
                    plugin_name=self.name,
                    message=f"Legacy commands cleaned up ({count} files removed)",
                )

            return PluginResult(
                success=True,
                plugin_name=self.name,
                message="No legacy commands to clean up",
            )
        except Exception as e:
            context.logger.error(f"  \u274c Failed to clean up commands: {e}")
            return PluginResult(
                success=False,
                plugin_name=self.name,
                message=f"Commands cleanup failed: {e!s}",
                errors=[str(e)],
            )

    def verify(self, context: InstallContext) -> PluginResult:
        """Verify legacy commands directory is gone.

        Args:
            context: InstallContext with shared installation utilities

        Returns:
            PluginResult indicating verification success or failure
        """
        target_commands_dir = context.claude_dir / "commands" / "nw"

        if target_commands_dir.exists():
            return PluginResult(
                success=False,
                plugin_name=self.name,
                message="Legacy commands/nw/ still exists after cleanup",
                errors=["Legacy commands directory not removed"],
            )

        return PluginResult(
            success=True,
            plugin_name=self.name,
            message="No legacy commands present (migrated to skills)",
        )
