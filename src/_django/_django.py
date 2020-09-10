import os
class Django:
    def __init__(self, project_name):
        self.project_name = project_name
        
    def create_project(self):
        os.system(f'django-admin startproject {self.project_name} {self.project_path}')

    def create_project_dir(self):
        os.makedirs(self.project_name)
        os.chdir(self.project_name)
        self.project_path = os.getcwd()