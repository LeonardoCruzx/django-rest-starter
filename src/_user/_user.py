import os
import shutil

class User:
    def __init__(self, project_path):
        self.path = project_path

    def add_template(self, template: str):
        path = os.path.dirname(os.path.abspath(__file__))
        path += f"\\{template}"
        shutil.copytree(path, self.path + "\\user")