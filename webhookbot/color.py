class Color:
    __slots__ = ('value',)

    def __init__(self, color: int):
        self.value = color

    def to_dict(self):
        return self.value

    @classmethod
    def red(cls):
        return cls(0xff0000)

    @classmethod
    def green(cls):
        return cls(0x00ff00)

    @classmethod
    def blue(cls):
        return cls(0x0000ff)

    @classmethod
    def black(cls):
        return cls(0x000000)

    @classmethod
    def white(cls):
        return cls(0xffffff)

    @classmethod
    def gray(cls):
        return cls(0x2d2d2d)
