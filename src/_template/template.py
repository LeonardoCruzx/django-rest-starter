import os
import shutil
from pathlib import Path

class Template:
    def __init__(self, project_path: str):
        self.project_path = project_path

    def _copy_tree(self, src, dst):
        for f in os.listdir(src):
            if(f == "__pycache__"):
                continue
            s = os.path.join(src, f)
            d = os.path.join(dst, f)
            shutil.copy2(s,d)

    def add_template(self, template: str, *args, **kwargs):
        src = os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1]
        src = "\\".join(src)
        module = f"\\{self.__module__}".split(".")[0]
        path = src + module
        path += f"\\{template}"

        if(kwargs.get("dir", None) is not None):
            shutil.copytree(path, self.project_path + f"\\{kwargs.get('dir')}")
        else:
            self._copy_tree(path, self.project_path)

    