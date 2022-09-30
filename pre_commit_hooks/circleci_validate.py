from __future__ import annotations


from typing import Sequence
import argparse
from pre_commit_hooks import util


def installation():
    util.cmd_output('sudo','apt','install','snapd',retcode=None)
    util.cmd_output('sudo','snap','install' ,'circleci',retcode=None)

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    installation()
    retval = 0
    for filename in args.filenames:
        try:
            util.cmd_output('circleci', 'config','validate',*args.filenames,retcode=None,okcode=255)
        except Exception as e:
            print(f'{filename}: Failed to validate ({e})')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
