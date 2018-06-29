from webhookbot.message import Message


class Embed(Message):
    def __init__(self, **kwargs):
        self.title = kwargs.pop('title', None)
        self.type = kwargs.pop('type', None)
        self.description = kwargs.pop('description', None)
        self.url = kwargs.pop('url', None)
        self.timestamp = kwargs.pop('timestamp', None)
        self.color = kwargs.pop('color', None)
        self.footer = kwargs.pop('footer', None)
        self.image = kwargs.pop('image', None)
        self.thumbnail = kwargs.pop('thumbnail', None)
        self.video = kwargs.pop('video', None)
        self.provider = kwargs.pop('provider', None)
        self.author = kwargs.pop('author', None)
        self.fields = kwargs.pop('fields', None)
