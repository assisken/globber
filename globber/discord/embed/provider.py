from globber.discord.webhook import Webhook


class Provider(Webhook):
    __slots__ = ('name', 'url')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.url = kwargs.pop('', None)
