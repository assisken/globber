from globber.discord.webhook import Webhook


class Field(Webhook):
    __slots__ = ('name', 'value', 'inline')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.value = kwargs.pop('value', None)
        self.inline = kwargs.pop('inline', False)