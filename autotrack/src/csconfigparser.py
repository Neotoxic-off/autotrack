from configparser import ConfigParser
from collections import OrderedDict

class CaseSensitiveConfigParser(ConfigParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.optionxform = str

    def _read(self, fp, fpname):
        """Preserve section key case."""
        elements = OrderedDict()
        super()._read(fp, fpname)
        for section in self._sections:
            elements[section] = self._sections[section]
        self._sections = elements
