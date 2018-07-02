from globber.discord.webhook import Webhook


class Thumbnail(Webhook):
    __slots__ = ('url', 'proxy_url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.proxy_url = kwargs.pop('proxy_url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)
