import discord
import os
from discord.ext import tasks
from discord.ext import commands
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
#CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/ping":
        await message.channel.send("pong")

client.run(TOKEN)
