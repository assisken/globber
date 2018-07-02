from globber.discord import Message


class Video(Message):
    __slots__ = ('url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)
