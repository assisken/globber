from globber.discord.webhook import Webhook


class Video(Webhook):
    __slots__ = ('url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)
