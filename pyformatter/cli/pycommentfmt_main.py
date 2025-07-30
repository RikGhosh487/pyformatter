import argparse
import sys
import os
from pyformatter.config import load_config
from pyformatter.utils import should_format_file


def main():
    """Main entry point for the script."""
    config = load_config("pycommentfmt")

    parser = argparse.ArgumentParser(description="Format Python comments.")
    parser.add_argument("files", nargs="+", help="Python files to format.")
    parser.add_argument(
        "--line-length",
        type=int,
        default=config.get("line_length", 88),
        help="Maximum line length for comments (default: 88).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if files are formatted correctly without modifying them.",
    )
    parser.add_argument(
        "--include",
        default=config.get("include", r"\.py"),
        help="Regex pattern for files to include.",
    )
    parser.add_argument(
        "--exclude",
        default=config.get("exclude", ""),
        help="Regex pattern for files to exclude.",
    )

    args = parser.parse_args()
    modified = False

    # Expand all files from directories, and apply filters
    all_files = []
    for path in args.files:
        if os.path.isdir(path):
            for root, _, filenames in os.walk(path):
                for fname in filenames:
                    full = os.path.join(root, fname)
                    if should_format_file(full, args.include, args.exclude):
                        all_files.append(full)
        else:
            if should_format_file(path, args.include, args.exclude):
                all_files.append(path)

    for path in all_files:
        # TODO: Import comment formatting logic here
        pass

    if modified:
        sys.exit(1)
