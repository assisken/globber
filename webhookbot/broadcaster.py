import asyncio
from asyncio import Future
from typing import Callable
from datetime import datetime
from aiofiles import open


class Broadcaster:
    type_stamp = {
        'info': {'long': 'INFO', 'short': 'I'},
        'error': {'long': 'ERROR', 'short': 'E'},
        'debug': {'long': 'DEBUG', 'short': 'D'}
    }

    def __init__(self, modes: tuple = (), **kwargs):
        self.modes = modes
        self.format = kwargs.pop('format', 'short')
        self.time_stamp = '%d-%m-%Y %H:%M:%S'
        self.stamp = '{time} [{state}] {content}\n'
        self.coros = []
        self.loop = asyncio.get_event_loop()

    def __getattr__(self, name: str):
        if name not in self.modes:
            def _(*args, **kwargs):
                pass
            return _

        def _missing(text):
            self.__send(self.type_stamp[name][self.format], text)
        return _missing

    def listener(self, coro: Callable):
        async def wrapper(future: Future, text: str):
            await coro(text)
            future.set_result(True)

        self.coros.append(wrapper)

    def __send(self, state: str, text: str):
        content = self.stamp.format(
            time=datetime.now().strftime(self.time_stamp),
            state=state,
            content=text
        )
        tasks = []
        for coro in self.coros:
            future = asyncio.Future()
            asyncio.ensure_future(coro(future, content))
            tasks.append(future)
        self.loop.run_until_complete(
            asyncio.gather(*tasks)
        )


broadcast = Broadcaster(('error', 'info', 'debug'))


@broadcast.listener
async def filer(text: str):
    async with open('log.txt', 'a') as file:
        await file.write(text)


@broadcast.listener
async def printer(text: str):
    print(text)


broadcast.error('Hello there!')
