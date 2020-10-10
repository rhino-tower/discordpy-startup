import discord
import os
from discord.ext import tasks
from discord.ext import commands
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']
bot = commands.Bot(command_prefix = '/')
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'これからよろしく！':
        message.channel.send("了解しました‼")

bot.run(TOKEN)
