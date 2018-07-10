import json
from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class Message(metaclass=ABCMeta):
    """
    Abstract class with methods that used to convert objects to dict and to json.
    """
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        """
        See :meth:`to_json`
        """
        return self.to_json()

    def to_dict(self) -> Dict[str, Any]:
        """
        Method that converts an object's fields to dict.

        Returns
        -------
        dict
            The converted object's fields as a dict.
        """
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
        """
        Method that converts an object's fields to json.

        Returns
        -------
        str
            The converted object's fields as a json.
        """
        return str(json.dumps(self.to_dict(), default=lambda o: o.to_dict()))
