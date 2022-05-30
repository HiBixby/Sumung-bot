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
    
bot.run(Token)#보안을위해 다른 코드(to.py)에서 토큰값을 가져옴.