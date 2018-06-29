from webhookbot.message import Message


class Webhook(Message):
    def __init__(self, **kwargs):
        self.content = kwargs.pop('content', None)
        self.username = kwargs.pop('username', None)
        self.avatar_url = kwargs.pop('avatar_url', None)
        self.tts = kwargs.pop('tts', False)
        self.file = None
        self.embeds = kwargs.pop('embeds', None)
