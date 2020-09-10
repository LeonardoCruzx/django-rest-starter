import os
import shutil
class Django:
    def __init__(self, project_name):
        self.project_name = project_name
        
    def create_project(self):
        os.system(f'django-admin startproject {self.project_name} {self.project_path}')

    def create_project_dir(self):
        os.makedirs(self.project_name)
        self.project_path = os.getcwd() + f"\\{self.project_name}"

    def add_template(self, template: str) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        path += f"\\{template}"
        self._copy_tree(path, self.project_path)

    def _copy_tree(self, src, dst):
        for f in os.listdir(src):
            s = os.path.join(src, f)
            d = os.path.join(dst, f)
            shutil.copy2(s,d)