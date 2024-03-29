from __future__ import annotations


from typing import Sequence
from pre_commit_hooks import util
import argparse


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            util.cmd_output('circleci', 'config','validate',filename)
        except util.CalledProcessError as e:
            print(f'{filename}: Failed to validate ({e})')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
