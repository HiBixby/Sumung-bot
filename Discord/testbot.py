import discord
from discord.ext import commands
from to import Token

bot=commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('나도 안녕!')

bot.run(Token)#토큰 보안