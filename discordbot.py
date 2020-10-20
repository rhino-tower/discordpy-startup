import discord
import os
from discord.ext import tasks
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']
client = discord.Client()

usage = '● 使い方 : 『-(課題名),(提出日)』と入力すると課題の締め切りが登録できます\n\n' \
    + '● (提出日) の書き方 : 年/月/日/時/分\n\n' \
    + '● (例) 2020年9月20日10時30分の場合\n　-(課題名),2020/9/20/10/30\n\n' \
    + '☆ 使い方を忘れたら『help』で、この説明は何度も見れます\n\n' \
    + '!注意! task_databaseチャンネルに課題内容を保管するので、書き込みは注意しましょう!'

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'help':
        await message.channel.send(usage)

client.run(TOKEN)
