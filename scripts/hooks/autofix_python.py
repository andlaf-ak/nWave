"""Auto-fix Python code quality issues before commit.

Runs ruff check --fix and ruff format on all staged .py files, then
re-stages any modified files. Always exits 0 — the fix is silent.

This eliminates the commit-retry loop where ruff reports issues,
the commit fails, we fix manually, retry, and burn tokens/minutes.
The CI pipeline still runs read-only ruff checks as a safety net.
"""

import subprocess
import sys


DIRS = ["src/", "scripts/", "tests/"]


def main() -> int:
    # Run ruff check with auto-fix
    subprocess.run(
        ["ruff", "check", "--fix", "--quiet", *DIRS],
        check=False,
    )

    # Run ruff format
    subprocess.run(
        ["ruff", "format", "--quiet", *DIRS],
        check=False,
    )

    # Re-stage any files that were modified by ruff
    result = subprocess.run(
        ["git", "diff", "--name-only", "--", "*.py"],
        capture_output=True,
        text=True,
        check=False,
    )
    modified = [f for f in result.stdout.splitlines() if f]
    if modified:
        subprocess.run(["git", "add", "--", *modified], check=False)
        for f in modified[:5]:
            print(f"Auto-fixed and re-staged: {f}")
        if len(modified) > 5:
            print(f"... and {len(modified) - 5} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())
