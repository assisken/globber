from typing import Tuple

import requests
from . import Message
from requests import Response

from .embed import Embed


class Webhook(Message):
    __slots__ = ('content', 'username', 'avatar_url', 'tts', 'file', 'embeds')

    def __init__(self, **kwargs):
        self.content: str = kwargs.pop('content', None)
        self.username: str = kwargs.pop('username', None)
        self.avatar_url: str = kwargs.pop('avatar_url', None)
        self.tts: bool = kwargs.pop('tts', False)
        self.file = None
        self.embeds: Tuple[Embed] = kwargs.pop('embeds', None)

    def post(self, url: str) -> Response:
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url=url,
                             data=self.to_json(),
                             headers=headers)
        return resp
