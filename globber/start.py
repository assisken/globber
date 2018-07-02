from pprint import pprint

from globber.discord.embed import *
from globber.webhook import Webhook
from globber.discord.embed.color import Color

url = 'https://confid.ru/data/avatars/L4SiJsaxM1DkAPC2rGOh8n4ZeKwthEi2.jpg'

author = OtherEmbed(name='assisken')
embed = Embed(
    title='testing',
    description='it',
    color=Color.blue(),
    timestamp=datetime.utcnow(),
    author=EmbedAuthor(name='assisken',
                       icon_url='https://confid.ru/data/avatars/L4SiJsaxM1DkAPC2rGOh8n4ZeKwthEi2.jpg'),
    footer=EmbedFooter(text='Haiaia', icon_url=url),
    image=EmbedImage(url=url),
    thumbnail=EmbedThumbnail(url=url),
    fields=(
        EmbedField(name='hmmm', value=':ok_hand:', inline=True),
        EmbedField(name='mmm', value=':joy:', inline=True)
    )
)
data = Webhook(content='Hello!', embeds=(embed,))

pprint(data.embeds[0].fields[0].to_dict())
res = data.post('https://ptb.discordapp.com/api/webhooks/462219841818984448'
                '/5FK6Q80Rk7KVyu_E0RB612Fihf1QRDcrnZ4IZtGdo6R_Ofz-oP3-g4lga7X1Ge60ETQM')
print(res)
