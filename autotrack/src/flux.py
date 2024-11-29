import requests

class Flux:
    def __init__(self, source_uri: str, path: str):
        self.source: str = source_uri
        self.path: str = path

    def download(self):
        r = self._invoker()

        if r.status_code == 200:
            with open(self.path, "w+") as f:
                f.write(r.text)
        print(f"request returned: {r.status_code}")

    def read(self):
        content: str = None

        with open(self.path, "r") as f:
            content = f.read().replace(r"\n", r"\\n")

        return repr(content)

    def _invoker(self):
        return requests.get(self.source)
