from globber.discord import Message


class Footer(Message):
    __slots__ = ('text', 'icon_url', 'proxy_icon_url')

    def __init__(self, **kwargs):
        self.text: str = kwargs.pop('text', None)
        self.icon_url = kwargs.pop('icon_url', None)
        self.proxy_icon_url = kwargs.pop('proxy_icon_url', None)