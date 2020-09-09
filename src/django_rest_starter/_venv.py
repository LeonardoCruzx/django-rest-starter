import os
import json

class Venv:
    def __init__(self, path):
        self.path = path + '\\.venv\\Scripts\\'

    def _get_requirements(self, key):
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)
        with open('requirements.json', 'r') as json_file:
            req_file = json.load(json_file)
            req = req_file[key]
            req = " ".join(req)
        return req