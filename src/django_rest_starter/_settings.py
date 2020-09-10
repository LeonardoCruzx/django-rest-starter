import os
import json

class Settings:
    def __init__(self, settings_path):
        self.path = settings_path

    def add_settings(self, settings: str):
        settings = self._get_settings(settings)
        os.chdir(self.path)
        with open('settings.py', 'a') as pf:
            for s in settings:
                pf.write("\n")
                for k,v in s.items():
                    pf.write(v + "\n")

    def _get_settings(self, settings: str) -> str:
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)
        with open('settings.json', 'r') as json_file:
            sett_file = json.load(json_file)
            sett = sett_file[settings]
        return sett