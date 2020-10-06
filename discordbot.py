import discord
import os
from discord.ext import tasks
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'これからよろしく！':
        print("了解しました‼")

@tasks.loop(seconds = 86400)
async def loop():
    dt = datetime.datetime.now()

    if dt.strftime('%A') == 'Monday':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('今日からソフトウェア技術とサイバー技術の課題が出ます！\nお忘れなく!')

loop.start()
client.run(TOKEN)
