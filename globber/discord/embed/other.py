from globber.discord.webhook import Webhook


class Other(Webhook):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return self.__dict__
