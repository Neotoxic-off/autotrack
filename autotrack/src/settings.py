import json

class Settings:
    def __init__(self):
        self.path: str = "settings.json"
        self.content: dict = {}

        self.load()

    def load(self):
        with open(self.path, "r") as f:
            self.content = json.loads(
                f.read()
            )

    def save(self):
        with open(self.path, "w+") as f:
            f.write(json.dumps(
                self.content
            ))
