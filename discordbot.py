import discord
import os
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime, timedelta
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
ANNOUNCE_CHANNEL_ID =  os.environ['ANNOUNCE_CHANNEL_ID']
DATABASE_CHANNEL_ID =  os.environ['DATABASE_CHANNEL_ID']
client = discord.Client()

usage = '◎ 使い方 : ①『-(課題名),(提出日)』と入力すると課題の締め切りが登録できます\n\n' \ 
    + '● (提出日) の書き方 : 年/月/日/時/分\n\n' \
    + '● (例) 2020年9月20日10時30分の場合\n　-(課題名),2020/9/20/10/30\n\n' \
    + '②『update』を入力すると、更新されます\n\n' \
    + '☆ 使い方を忘れたら『help』で、この説明は何度も見れます\n\n' \
    + '!注意! task_databaseチャンネルに課題内容を保管するので、書き込みは注意しましょう!'

def time_limit_msg(date_dict):
    y = int(date_dict['year'])
    m = int(date_dict['month'])
    d = int(date_dict['day'])
    h = int(date_dict['hour'])
    M = int(date_dict['minute'])

    dt_deadline = datetime(year=y, month=m, day=d, hour=h, minute=M)
    dt_now = datetime.now() + timedelta(hours=9)
    left_time = dt_deadline - dt_now
    
    if dt_deadline < dt_now:
        return

    seconds = left_time.seconds % 60
    minute = int(left_time.seconds / 60) % 60
    hour = int(int(left_time.seconds / 60) / 60)
    msg = "\n現在の時刻 : " + str(dt_now)
    msg += "\n========提出まで残り時間========\n"
    msg += str(left_time.days) + "日" + str(hour) + "時間" + str(minute) + "分" + str(seconds) + "秒\n"
    if left_time.days == 0:
        msg += "残り一日を切っています!!"
    msg += "```"
    return msg

async def time_limit(register_channel):
    channel = client.get_channel(int(ANNOUNCE_CHANNEL_ID))
    text_id_list = await register_channel.history().flatten()
    msg = ""
    for text_id in text_id_list:
        text = text_id.content
        i = 1
        msg += "```課題名 : "
        while text[i] != ',':
            msg += text[i]
            i += 1
        i += 1

        date_dict = {'year' : '0', 'month' : '0', 'day' : '0', 'hour' : '0', 'minute' : '0'}
        
        while '0' <= text[i] and text[i] <= '9':
            date_dict['year'] += text[i]
            i += 1
        i += 1
        while '0' <= text[i] and text[i] <= '9':
            date_dict['month'] += text[i]
            i += 1
        i += 1
        while '0' <= text[i] and text[i] <= '9':
            date_dict['day'] += text[i]
            i += 1
        i += 1
        while '0' <= text[i] and text[i] <= '9':
            date_dict['hour'] += text[i]
            i += 1
        i += 1
        while i != len(text):
            date_dict['minute'] += text[i]
            i += 1
        msg += time_limit_msg(date_dict)
    await channel.send(msg)

async def update_task():
    channel = client.get_channel(int(DATABASE_CHANNEL_ID))
    await time_limit(channel)

@client.event
async def on_ready():
    await update_task()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'help':
        await message.channel.send(usage)
    elif message.content == 'update':
        await update_task()
    elif message.content.startswith('-'):
        channel = client.get_channel(int(DATABASE_CHANNEL_ID))
        await channel.send(message.content)
        await time_limit(channel)

client.run(TOKEN)
