import json
import asyncio

from datetime import datetime
import discord
from aiohttp import web
import requests


# client = discord.Client()
from webhookbot.embed import Embed
from webhookbot.webhook import Webhook


async def handle(request):
    mention_id = request.query.get('mention_id', None)
    mention = f'<@!{mention_id}>:\n' if mention_id else ''
    text = request.query.get('text', '')
    out = f'{mention}{text}'
    await send_message(out)
    return web.Response(text='Success')


async def send_message(text):
    await client.wait_until_ready()
    channel = discord.Object(id=452495339136614411)
    await client.send_message(channel, text)


async def start():
    app = web.Application()
    app.add_routes([
        web.get('/tg', handle),
    ])
    await client.wait_until_ready()
    runner = web.AppRunner(app=app)
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=5001)
    await site.start()


# loop = asyncio.get_event_loop()
# tasks = [
#     loop.create_task(client.start('NDUyNDk0NDQyNjcxMzc0MzQ2.DhcVgA.TdoC_Dwj7bUN8urAdbP1eN8IMfk')),
#     loop.create_task(start())
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

headers = {
    'Content-Type': 'application/json'
}

embed = Embed(title='testing', description='it', color=0xffffff, type='rich')
data = Webhook(content='Hello!', embeds=[embed])

resp = requests.post(
    url='https://ptb.discordapp.com/api/webhooks/462219841818984448/5FK6Q80Rk7KVyu_E0RB612Fihf1QRDcrnZ4IZtGdo6R_Ofz'
        '-oP3-g4lga7X1Ge60ETQM',
    data=data.to_json(),
    headers=headers
)

print(data)
