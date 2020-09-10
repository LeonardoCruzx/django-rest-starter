class Settings:
    def __init__(self):
        pass

    def _get_settings(self, settings: str) -> str:
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)
        with open('settings.json', 'r') as json_file:
            sett_file = json.load(json_file)
            sett = sett_file[settings]
            sett = " ".join(sett)
        return sett