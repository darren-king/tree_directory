# Provides the CLI for the application

import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(
        root_dir
    )  # Create an instance of the DirectoryTree object with the root directory as an argument
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="Tree",
        description="A Directory Tree Generator",
        epilog="Thank you for using the Directory Tree Generator",
    )
    parser.version = f"Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",  # Sets the current directory as the default root directory
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()
