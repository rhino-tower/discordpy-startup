import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

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
        await message.channel.send('了解しました！！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
