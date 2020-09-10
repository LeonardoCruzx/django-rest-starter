from _user._user import User
from _django._django import Django
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
    django = Django(args.project_name)
    django.create_project_dir()
    venv = Venv()
    venv.create_venv()
    venv.install_requirements("base_requirements")
    django.create_project()
    settings = Settings(django.project_path + f"\\{args.project_name}")
    settings.add_settings("base_settings")
    if(args.user):
        user = User(django.project_path)
        user.add_template("base_template")
        venv.install_requirements("user_requirements")
        settings.add_settings("user_settings")
    if(args.heroku):
        pass

if __name__ == "__main__":
    sys.exit(main())