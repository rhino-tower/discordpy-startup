import discord
import os
import discord.ext import tasks
import datetime
import locale

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'これからよろしく！':
        await message.channel.send('了解しました!!')
@tasks.loop(seconds = 86400)
async def loop():
    dt = datetime.datetime.now()

    if dt.strftime('%A') == 'Monday':
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send('今日からソフトウェア技術とサイバー技術の課題が出ます！\nお忘れなく!')

loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
