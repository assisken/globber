from typing import Union, Tuple, Optional
from datetime import datetime

from globber.discord.embed.color import Color
from globber.discord.embed.author import Author
from globber.discord.embed.field import Field
from globber.discord.embed.footer import Footer
from globber.discord.embed.image import Image
from globber.discord.embed.provider import Provider
from globber.discord.embed.thumbnail import Thumbnail
from globber.discord.embed.video import Video
from globber.discord import Message


class Embed(Message):
    """
    An embed message that used in discord.

    Attributes
    ----------
    title : str
        Title of the embed message.
    type : str
        Type of the embed message. Always "rich" for webhooks.
    description : str
        Description of the embed message.
    url : str
        Url of the embed message.
    timestamp : datetime
        Timestamp of the embed message.
    color : :class:`Color`
        Color of the embed message.
    footer : :class:`Footer`
        Footer of the embed message.
    image : :class:`Image`
        Image of the embed message.
    thumbnail : :class:`Thumbnail`
        Thumbnail of the embed message.
    video : :class:`Video`
        Video of the embed message.
    provider : :class:`Provider`
        Provider of the embed message.
    author : :class:`Author`
        Author of the embed message.
    field : tuple of :class:`Field`
        Field of the embed message.
    """

    __slots__ = ('title', 'type', 'description', 'url', '__timestamp',
                 '__color', '__footer', '__image', '__thumbnail', '__video',
                 '__provider', '__fields', '__author')

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

    @property
    def author(self) -> Optional[Author]:
        return getattr(self, '__author', None)

    @author.setter
    def author(self, value: Union[Author, None]):
        if value is None:
            pass
        elif isinstance(value, Author):
            setattr(self, '__author', value)
        else:
            raise ValueError('Expected Author, got {}'.format(type(value)))

    @property
    def color(self) -> Optional[Color]:
        return getattr(self, '__color', None)

    @color.setter
    def color(self, value: Optional[Union[Color, int]]):
        if value is None:
            pass
        elif isinstance(value, Color):
            setattr(self, '__color', value)
        elif isinstance(value, int):
            setattr(self, '__color', Color(value))
        else:
            raise TypeError('Expected Color or int, got {}'.format(type(value)))

    @property
    def timestamp(self) -> Optional[str]:
        attr: datetime = getattr(self, '__timestamp', None)
        return attr.isoformat()

    @timestamp.setter
    def timestamp(self, value: Optional[Union[datetime, float]]):
        if value is None:
            pass
        elif isinstance(value, datetime):
            setattr(self, '__timestamp', value)
        elif isinstance(value, float):
            setattr(self, '__timestamp', datetime.fromtimestamp(value))
        else:
            raise TypeError('Expected datetime or float, got {}'.format(type(value)))

    @property
    def thumbnail(self) -> Optional[Thumbnail]:
        return getattr(self, '__thumbnail', None)

    @thumbnail.setter
    def thumbnail(self, value: Optional[Thumbnail]):
        if value is None:
            pass
        elif isinstance(value, Thumbnail):
            setattr(self, '__thumbnail', value)
        else:
            raise TypeError('Thumbnail expected, got {}'.format(type(value)))

    @property
    def footer(self) -> Optional[Footer]:
        return getattr(self, '__footer', None)

    @footer.setter
    def footer(self, value: Optional[Footer]):
        if value is None:
            pass
        elif isinstance(value, Footer):
            setattr(self, '__footer', value)
        else:
            raise TypeError('Footer expected, got {}'.format(type(value)))

    @property
    def fields(self) -> Optional[Tuple[Field]]:
        return getattr(self, '__fields', None)

    @fields.setter
    def fields(self, value: Optional[Tuple[Field]]):
        if value is None:
            pass
        elif isinstance(value, tuple):
            setattr(self, '__fields', value)
        else:
            raise TypeError('Expected Iterable or tuple, got {}'.format(type(value)))

    @property
    def provider(self) -> Optional[Provider]:
        return getattr(self, '__provider', None)

    @provider.setter
    def provider(self, value: Optional[Provider]):
        if value is None:
            pass
        elif isinstance(value, Provider):
            setattr(self, '__provider', value)
        else:
            raise TypeError('Expected Provider, got {}'.format(type(value)))

    @property
    def image(self) -> Optional[Image]:
        return getattr(self, '__image', None)

    @image.setter
    def image(self, value: Optional[Image]):
        if value is None:
            pass
        elif isinstance(value, Image):
            setattr(self, '__image', value)
        else:
            raise TypeError('Expected Image, got {}'.format(type(value)))

    @property
    def video(self) -> Optional[Video]:
        return getattr(self, '__video', None)

    @video.setter
    def video(self, value: Video):
        if value is None:
            pass
        elif isinstance(value, Video):
            setattr(self, '__video', value)
        else:
            raise TypeError('Expected Video, got {}'.format(type(value)))
