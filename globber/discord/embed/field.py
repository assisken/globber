from globber.discord import Message


class Field(Message):
    __slots__ = ('name', 'value', 'inline')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.value = kwargs.pop('value', None)
        self.inline = kwargs.pop('inline', False)