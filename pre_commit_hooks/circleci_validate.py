from __future__ import annotations


from typing import Sequence
from pre_commit_hooks import util
import argparse
import os
import logging


def installation():
    util.cmd_output('sudo','apt','install','snapd')
    util.cmd_output('sudo','snap','install' ,'circleci')

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    installation()
    retval = 0
    for filename in args.filenames:
        try:
            util.cmd_output('circleci', 'config','validate',*args.filenames)
        except util.CalledProcessError as e:
            print(f'{filename}: Failed to validate ({e})')
            retval = 1
    return retval


if __name__ == '__main__':
    env_val = os.Getenv('CIRCLECI')
    print('Printing env value: ',env_val)


    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Env log value',env_val)
    if env_val != 'true':
        raise SystemExit(main())
