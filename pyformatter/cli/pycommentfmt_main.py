import argparse
import logging
import os
import re
import sys

from pyformatter.config import load_config
from pyformatter.formatters.pycommentfmt import format_comments
from pyformatter.utils import should_format_file


def main():
    """Main entry point for the script."""

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("pycommentfmt")

    config = load_config("pycommentfmt", logger)

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

    compiled_include = re.compile(args.include)
    compiled_exclude = re.compile(args.exclude) if args.exclude else None

    # Expand all files from directories, and apply filters
    all_files = []
    for path in args.files:
        if os.path.isdir(path):
            for root, _, filenames in os.walk(path):
                for fname in filenames:
                    full = os.path.join(root, fname)
                    if should_format_file(full, compiled_include, compiled_exclude):
                        all_files.append(full)
        else:
            if should_format_file(path, compiled_include, compiled_exclude):
                all_files.append(path)

    for path in all_files:
        changed = format_comments(path, args.line_length, args.check)
        if changed:
            modified = True

    if args.check and modified:
        sys.exit(1)
