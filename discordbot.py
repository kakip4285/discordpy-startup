from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
import discord

TOKEN = "ODYzNDMxMjQyMDAzNjQ0NDM2.YOmzAQ.pB41IIWNA99MriQSGNEKue2jaMI"

client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
          # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/pick':
        await message.channel.send(y)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

python-3.9

discord.py

discordbot: python discordbot.py


bot.run(token)
