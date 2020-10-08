import discord
from discord.ext import commands
from discord.ext import tasks
import datetime
import locale

bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']

client = discord.Client()
channel = client.get_channel(CHANNEL_ID)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'これからよろしく！':
        await message.channel.send("了解しました‼")

@tasks.loop(seconds = 10)
async def loop():
    await channel.send('うるさくてごめんなさい') 

@tasks.loop(seconds = 86400)
async def loop():
    dt = datetime.datetime.now()

    if dt.strftime('%A') == 'Monday':
        await channel.send('今日からソフトウェア技術とサイバー技術の課題が出ます！\nお忘れなく!')

loop.start()
bot.run(TOKEN)
