from globber.discord import Message
from typing import Dict, Any


class Other(Message):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
