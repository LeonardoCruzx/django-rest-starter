import user
from django_rest_starter._venv import Venv

import sys
import os

from argparse import ArgumentParser
from typing import Any

def main() -> Any:
    parser = ArgumentParser()
    parser.add_argument('project_name', help='project name')
    parser.add_argument('--user', help='add user template', default=False, const=True, nargs="?")
    parser.add_argument('--heroku', help='add heroku config', default=False, const=True, nargs="?")
    args = parser.parse_args()
    if(args.user):
        pass
    if(args.heroku):
        pass

if __name__ == "__main__":
    sys.exit(main())