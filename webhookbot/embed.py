from color import Color
from webhookbot.message import Message
from typing import Union, Iterator
from datetime import datetime


class OtherEmbed(Message):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return self.__dict__


class EmbedAuthor(Message):
    __slots__ = ('name', 'url', 'icon_url', 'proxy_icon_url')

    def __init__(self, **kwargs):
        self.name: str = kwargs.pop('name', None)
        self.url: str = kwargs.pop('url', None)
        self.icon_url: str = kwargs.pop('icon_url', None)
        self.proxy_icon_url: str = kwargs.pop('proxy_icon_url', None)


class EmbedFooter(Message):
    __slots__ = ('text', 'icon_url', 'proxy_icon_url')

    def __init__(self, **kwargs):
        self.text: str = kwargs.pop('text', None)
        self.icon_url = kwargs.pop('icon_url', None)
        self.proxy_icon_url = kwargs.pop('proxy_icon_url', None)


class EmbedField(Message):
    __slots__ = ('name', 'value', 'inline')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.value = kwargs.pop('value', None)
        self.inline = kwargs.pop('inline', False)


class EmbedProvider(Message):
    __slots__ = ('name', 'url')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.url = kwargs.pop('', None)


class EmbedImage(Message):
    __slots__ = ('url', 'proxy_url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.proxy_url = kwargs.pop('proxy_url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)


class EmbedVideo(Message):
    __slots__ = ('url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)


class EmbedThumbnail(Message):
    __slots__ = ('url', 'proxy_url', 'height', 'width')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url', None)
        self.proxy_url = kwargs.pop('proxy_url', None)
        self.height = kwargs.pop('height', None)
        self.width = kwargs.pop('width', None)


class Embed(Message):
    __slots__ = ('title', 'type', 'description', 'url', '__timestamp',
                 '__color', '__footer', '__image', '__thumbnail', '__video',
                 '__provider', '__fields', '__author')

    def __init__(self, **kwargs):
        self.title = kwargs.pop('title', None)
        self.type = kwargs.pop('type', None)
        self.description = kwargs.pop('description', None)
        self.url = kwargs.pop('url', None)

        self.footer = kwargs.pop('footer', None)
        self.provider = kwargs.pop('provider', None)
        self.video = kwargs.pop('video', None)
        self.image = kwargs.pop('image', None)
        self.author = kwargs.pop('author', None)
        self.color = kwargs.pop('color', None)
        self.timestamp = kwargs.pop('timestamp', None)
        self.thumbnail = kwargs.pop('thumbnail', None)
        self.fields = kwargs.pop('fields', None)

    @property
    def author(self):
        return getattr(self, '__author', None)

    @author.setter
    def author(self, value: EmbedAuthor):
        if value is None:
            pass
        elif isinstance(value, EmbedAuthor):
            setattr(self, '__author', value)
        else:
            raise ValueError('Expected EmbedAuthor, got {}'.format(type(value)))

    @property
    def color(self):
        return getattr(self, '__color', None)

    @color.setter
    def color(self, value: Union[Color, int]):
        if value is None:
            pass
        elif isinstance(value, Color):
            setattr(self, '__color', value)
        elif isinstance(value, int):
            setattr(self, '__color', Color(value))
        else:
            raise TypeError('Expected Color or int, got {}'.format(type(value)))

    @property
    def timestamp(self):
        attr: datetime = getattr(self, '__timestamp', None)
        return attr.isoformat()

    @timestamp.setter
    def timestamp(self, value: Union[datetime, float]):
        if value is None:
            pass
        elif isinstance(value, datetime):
            setattr(self, '__timestamp', value)
        elif isinstance(value, float):
            setattr(self, '__timestamp', datetime.fromtimestamp(value))
        else:
            raise TypeError('Expected datetime or float, got {}'.format(type(value)))

    @property
    def thumbnail(self):
        return getattr(self, '__thumbnail', None)

    @thumbnail.setter
    def thumbnail(self, value: EmbedThumbnail):
        if value is None:
            pass
        elif isinstance(value, EmbedThumbnail):
            setattr(self, '__thumbnail', value)
        else:
            raise TypeError('EmbedThumbnail expected, got {}'.format(type(value)))

    @property
    def footer(self):
        return getattr(self, '__footer', None)

    @footer.setter
    def footer(self, value: EmbedFooter):
        if value is None:
            pass
        elif isinstance(value, EmbedFooter):
            setattr(self, '__footer', value)
        else:
            raise TypeError('EmbedFooter expected, got {}'.format(type(value)))

    @property
    def fields(self):
        return getattr(self, '__fields', None)

    @fields.setter
    def fields(self, value: Union[Iterator, tuple]):
        if value is None:
            pass
        elif isinstance(value, tuple):
            setattr(self, '__fields', value)
        elif isinstance(value, Iterator):
            setattr(self, '__fields', tuple(value))
        else:
            raise TypeError('Expected Iterable or tuple, got {}'.format(type(value)))

    @property
    def provider(self):
        return getattr(self, '__provider', None)

    @provider.setter
    def provider(self, value: EmbedProvider):
        if value is None:
            pass
        elif isinstance(value, EmbedProvider):
            setattr(self, '__provider', value)
        else:
            raise TypeError('Expected EmbedProvider, got {}'.format(type(value)))

    @property
    def image(self):
        return getattr(self, '__image', None)

    @image.setter
    def image(self, value: EmbedImage):
        if value is None:
            pass
        elif isinstance(value, EmbedImage):
            setattr(self, '__image', value)
        else:
            raise TypeError('Expected EmbedImage, got {}'.format(type(value)))

    @property
    def video(self):
        return getattr(self, '__video', None)

    @video.setter
    def video(self, value: EmbedVideo):
        if value is None:
            pass
        elif isinstance(value, EmbedVideo):
            setattr(self, '__video', value)
        else:
            raise TypeError('Expected EmbedVideo, got {}'.format(type(value)))
