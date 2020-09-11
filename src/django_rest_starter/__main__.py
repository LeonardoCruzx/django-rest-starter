from _user._user import User
from _django._django import Django
from django_rest_starter._settings import Settings
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
    
    #creates dir of the project
    django = Django(os.getcwd() + f"\\{args.project_name}")
    django.create_project_dir()

    #creates .venv and install the base requirements
    venv = Venv(django.project_path)
    venv.create_venv()
    venv.install_requirements("base_requirements")

    #use django admin to start the project
    django.create_project()
    django.add_template("base_template")

    #add base settings to the project
    settings = Settings(django.project_path + f"\\{django.project_name}")
    settings.add_settings("base_settings")

    if(args.user):
        user = User(django.project_path)
        user.add_template("base_template", dir="user")
        venv.install_requirements("user_requirements")
        settings.add_settings("user_settings")
    if(args.heroku):
        pass

if __name__ == "__main__":
    sys.exit(main())