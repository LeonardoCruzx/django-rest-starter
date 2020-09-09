import os
import json

class Venv:
    def __init__(self, path: str):
        self.path = path + '\\.venv\\Scripts\\'

    def _get_requirements(self, requirements: str) -> str:
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)
        with open('requirements.json', 'r') as json_file:
            req_file = json.load(json_file)
            req = req_file[requirements]
            req = " ".join(req)
        return req

    def install_requirements(self, requirements: str) -> None:
        req = self._get_requirements(requirements)
        os.chdir(self.path)
        os.system(f"pip install {req}")