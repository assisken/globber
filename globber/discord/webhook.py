from typing import Tuple

import requests
from . import Message
from requests import Response
from aiohttp import ClientSession

from .embed import Embed


class Webhook(Message):
    """
    Discord Webhook class.
    Used for sending webhooks to discord.

    Attributes
    ----------
    content : str
        The webhook's message contents (up to 2000 characters).
    username : str
        Override the default username of the webhook.
    avatar_url : str
        Override the default avatar of the webhook.
    tts : bool
        true if this is a TTS message.
    embeds: Tuple of :class:`embed.Embed`
        Embedded rich content.
    """
    __slots__ = ('content', 'username', 'avatar_url', 'tts', 'embeds')

    def __init__(self, **kwargs):
        self.content: str = kwargs.pop('content', None)
        self.username: str = kwargs.pop('username', None)
        self.avatar_url: str = kwargs.pop('avatar_url', None)
        self.tts: bool = kwargs.pop('tts', False)
        self.embeds: Tuple[Embed] = kwargs.pop('embeds', None)

    async def post(self, url: str) -> Response:
        """|coroutine|

        Makes post request to ``url`` by sending webhook json data.

        Parameters
        ----------
        url : str
            The url of webhook.

        Returns
        -------
        Response
        """
        session = ClientSession()
        headers = {'Content-Type': 'application/json'}
        resp = await session.post(url=url,
                                  data=self.to_json(),
                                  headers=headers)
        # resp = request.post(url=url,
        #                     data=self.to_json(),
        #                     headers=headers)
        await session.close()
        return resp
