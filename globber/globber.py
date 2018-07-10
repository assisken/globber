import asyncio
from asyncio import Future
from datetime import datetime
from enum import Enum, auto
from typing import Callable, Tuple


class State(Enum):
    """
    Enum for state that will be broadcast to listeners.
    """
    debug = auto()
    info = auto()
    error = auto()
    critical = auto()


class Globber:
    """
    Class that broadcasts text to listeners.

    Attributes
    ----------
    modes : Tuple[State, ...]
        Broadcaster's modes.
    time_stamp : str
        Timestamp of output text
    stamp : str
        Stamp of output text
    """

    def __init__(self, modes: Tuple[State, ...] = (), **kwargs):
        self.modes = modes
        self.time_stamp = '%d-%m-%Y %H:%M:%S'
        self.stamp = '{time} [{state}] {content}\n'
        self.__coros = []
        self.__loop = asyncio.get_event_loop()
        self.__format = kwargs.pop('format', 'short')

    def __getattr__(self, name: str):
        """
        A magic method that suppresses methods that not included in :attr:`modes`.
        The rest of them will broadcast message to listeners.

        Parameters
        ----------
        name : str
            Name of calling method.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python

           broadcaster = Globber((State.info))
           @broadcaster.listener
           async def printer(text):
               print(text)

           broadcaster.info('Info text')
           broadcaster.error('Will be suppressed')

        Output:

        .. code-block:: none

           01-01-1971 12:12:12 [INFO] Info text
        """
        def _missing(text):
            self.__send(state, text)

        def _(*args, **kwargs):
            pass

        for mode in self.modes:
            if name == mode.name:
                state = mode
                return _missing
        else:
            return _

    def listener(self, coro: Callable):
        """
        A decorator that adds listener.

        Parameters
        ----------
        coro : Callable
            Listener's function.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python

           broadcaster = Globber((State.info))

           @broadcaster.listener
           async def printer(text):
               print('Printing message:')
               print(text)

           broadcaster.info('Info text')

        Output:

        .. code-block:: none

           Printing message:
           01-01-1971 12:12:12 [INFO] Info text
        """
        async def wrapper(future: Future, text: str, **kwargs):
            await coro(text, **kwargs)
            future.set_result(True)

        self.__coros.append(wrapper)

    def __send(self, state: State, text: str):
        kwargs = {
            'time': datetime.utcnow().strftime(self.time_stamp),
            'state': state.name.upper(),
            'content': text
        }
        tasks = []
        for coro in self.__coros:
            future = asyncio.Future()
            asyncio.ensure_future(coro(future, self.stamp.format(**kwargs), **kwargs))
            tasks.append(future)
        self.__loop.run_until_complete(
            asyncio.gather(*tasks)
        )
