from src.flux import Flux
from src.settings import Settings
from src.csconfigparser import CaseSensitiveConfigParser

class Core:
    def __init__(self):
        self.configparser: CaseSensitiveConfigParser = CaseSensitiveConfigParser()
        self.settings: Settings = Settings()
        self.flux: Flux = Flux(
            self.settings.content.get("flux"),
            "{}.trackers".format(self.settings.content["qbittorrent"]["config"])
        )

    def run(self):
        print("downloading new trackers")
        self.flux.download()

        self._load()
        self._save()

    def _load(self):
        print("loading qbittorent config")

        self._load_qbittorent_config()
        self._replace_trackers()

    def _save(self):
        print("saving qbittorent config")
        with open(self.settings.content["qbittorrent"]["config"], 'w') as f:
            self.configparser.write(f)
        print("saved qbittorent config")

    def _replace_trackers(self):
        section: str = self.settings.content["qbittorrent"]["section"]
        section_key: str = self.settings.content["qbittorrent"]["section_key"]

        self.configparser[section][section_key] = self.flux.read()

    def _load_qbittorent_config(self):
        self.configparser.read(self.settings.content["qbittorrent"]["config"])

    def _display_qbittorent_config(self):
        print(self.configparser.sections())
