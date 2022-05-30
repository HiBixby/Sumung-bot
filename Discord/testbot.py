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

@bot.command()
async def 공지(ctx):
    embed=discord.Embed(title="상명라운지 | 통합공지 게시판목록 | 상명라운지", url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srUpperNoticeYn=on&article.offset=0", description="통합공지 조회", color=0x2e35ff)
    embed.set_author(name="상명대학교 알리미 슴우")
    embed.set_thumbnail(url="https://www.smu.ac.kr/favicon.ico")
    embed.add_field(name="[naver](http://naver.com)", value="[naver](http://naver.com)", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.set_footer(text="1 페이지")
    await ctx.send(embed=embed)




bot.run(Token)#토큰 보안