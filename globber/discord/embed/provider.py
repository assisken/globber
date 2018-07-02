from globber.discord import Message


class Provider(Message):
    __slots__ = ('name', 'url')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.url = kwargs.pop('', None)
