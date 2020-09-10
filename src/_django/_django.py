import os
import shutil
from _template.template import Template

class Django(Template):
        
    def create_project(self):
        os.system(f'django-admin startproject {self.project_name} {self.project_path}')

    def create_project_dir(self):
        self.project_name = self.project_path.split("\\")[-1]
        os.makedirs(self.project_name)
        self.project_path = os.getcwd() + f"\\{self.project_name}"