from globber.discord.webhook import Webhook


class Author(Webhook):
    __slots__ = ('name', 'url', 'icon_url', 'proxy_icon_url')

    def __init__(self, **kwargs):
        self.name: str = kwargs.pop('name', None)
        self.url: str = kwargs.pop('url', None)
        self.icon_url: str = kwargs.pop('icon_url', None)
        self.proxy_icon_url: str = kwargs.pop('proxy_icon_url', None)