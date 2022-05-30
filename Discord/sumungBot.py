import discord
from discord.ext import commands
from discord.ext import tasks
import os
from Scraping import getNotice

bot=commands.Bot(command_prefix='수뭉아 ')

@tasks.loop(seconds=60.0)
async def my_background_task():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="슴우 목소리"))
    await bot.change_presence(activity=discord.Game(name="수뭉아 도움말"))
    await bot.change_presence(activity=discord.Game(name=f"서버 {len(bot.guilds)}개 참가"))

@bot.event
async def on_ready():
    print('수뭉봇에 로그인중입니다. ')
    print(f"봇={bot.user.name}(으)로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="수뭉아 도움말"))

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('수뭉이도 안녕!')

@bot.command()
async def 도움말(ctx):
    await ctx.channel.send('수뭉아 공지 `페이지(정수)` `한번에 볼 공지 개수(1~10)`\n'+'ex)수뭉아 공지 2 10\n'+"2페이지 공지사항 10개를 보여줍니다.",delete_after=60.0)
    await ctx.channel.send('ex)수뭉아 공지 2 10\n'+"1페이지 공지사항 5개를 보여줍니다.",delete_after=60.0)
    await ctx.message.delete(delay=60.0)

#pass_context=True
@bot.command()
async def 공지(ctx,arg1=1,arg2=5):
    embed=getNotice.createEmbedNotice(int(arg1),int(arg2))
    botmsg=await ctx.reply("안녕 슴우! 이 메세지는 1분 뒤에 지워질거야 :blush: ",embed=embed,delete_after=60.0) #임베드 메세지 보내고 1분 뒤 삭제
    await ctx.message.delete(delay=60.0) #사용자가 보낸 명령어 메세지를 1분 뒤에 삭제
    await botmsg.edit()


TOKEN=os.environ.get('BOT_TOKEN')
bot.run(TOKEN)#토큰 보안