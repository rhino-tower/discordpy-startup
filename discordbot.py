import discord
import os
from discord.ext import tasks
from discord.ext import commands
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']
client = discord.Client()

@tasks.loop(seconds = 10)
async def loop():
    channel = client.get_channel(int(CHANNEL_ID))
    await channel.send("ok")
"""
@tasks.loop(seconds = 86400)
async def loop():
    dt = datetime.datetime.now()

    if dt.strftime('%A') == 'Monday':
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send('今日からソフトウェア技術の課題が出ます！お忘れなく!')
"""
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/ping":
        await message.channel.send("pong")

loop.start()
client.run(TOKEN)
