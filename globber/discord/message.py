import json
from typing import Dict


class Message:
    def __str__(self):
        return self.to_json()

    def to_dict(self) -> Dict[str, 'Message']:
        result = {}
        for name in self.__slots__:
            if name[:2] == '__':
                name = name[2:]
            elif name[:1] == '_':
                name = name[1:]

            value = getattr(self, name)
            if value is None:
                continue

            result[name] = value
        return result

    def to_json(self) -> str:
        return str(json.dumps(self.to_dict(), default=lambda o: o.to_dict()))
