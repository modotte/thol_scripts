#!/usr/bin/env python

import sys
import re
import os
from pathlib import Path
import argparse

prog_path = sys.argv[0]

default_data_dir = "."
parser = argparse.ArgumentParser(
    description='Print relevant 2HOL sprites from an object.',
    formatter_class=argparse.RawTextHelpFormatter,
    epilog=f"""
  - If second argument is not provided, it will default to current directory.
  - For convenience, the pattern matching is made case insensitive and 
    anchored with ^PATTERN$ for exact case matching.
  - To autoload sprites with GIMP, pipe at the end with: | xargs gimp

  Example: {prog_path} 'turkey'
  Example with GIMP: {prog_path} 'turkey' ./OneLifeData7 | xargs gimp

""")

parser.add_argument(
    "description_pattern",
    type=str,
    help="object description to match. Python regex compatible")
parser.add_argument("data_dir",
                    type=str,
                    default=default_data_dir,
                    nargs="?",
                    help="data directory path [defaults: . ]")
args = parser.parse_args()


data_dir = args.data_dir

if not os.path.isdir(data_dir):
    print(f"error: {data_dir} is not a valid directory\n", file=sys.stderr)
    parser.print_help()
    sys.exit(1)

def is_valid_data_dir(path: str) -> bool:
    sprites_dir = os.path.join(path, "sprites")
    objects_dir = os.path.join(path, "objects")

    return os.path.isdir(sprites_dir) and os.path.isdir(objects_dir)

if not is_valid_data_dir(data_dir):
    print(
        f"error: {data_dir} dir does not contain sprites and object directories\n",
        file=sys.stderr)
    parser.print_help()
    sys.exit(1)

description = args.description_pattern
pattern = re.compile(f"^{description}$", re.IGNORECASE)
if len(description) == 0:
    print("error: object description to match cannot be empty\n",
          file=sys.stderr)
    parser.print_help()
    sys.exit(1)

object_files = list(Path(data_dir, "objects").glob("[0-9]*.txt"))


def get_sprite_ids(lines: list[str]) -> set[str]:
    as_id = lambda x: x.split("=")[1].strip()
    return set([as_id(line) for line in lines[1:] if "spriteID" in line])


def print_tga_filepaths(sprite_ids: set[str], target_dir: str):
    for idx in sprite_ids:
        tga_filename = idx + ".tga"
        filepath = os.path.join(target_dir, "sprites", tga_filename)

        print(filepath)


for file in object_files:
    with open(file, "r") as FD:
        lines = FD.readlines()
        description = lines[1]

        if pattern.match(description):
            print_tga_filepaths(get_sprite_ids(lines), data_dir)
