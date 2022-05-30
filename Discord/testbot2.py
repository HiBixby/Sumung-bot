import discord
from discord.ext import commands
from to import Token
import requests
from bs4 import BeautifulSoup
import re


bot=commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    print('test2 로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('test2도 안녕!')



@bot.command()
async def 공지(ctx):
    response = requests.get("https://www.smu.ac.kr/lounge/notice/notice.do?srUpperNoticeYn=on")
    html=response.text
    soup=BeautifulSoup(html,'lxml')

    webTitle=soup.find("title").get_text()

    content_titles=soup.find_all("dt",attrs={"class":re.compile("^board-thumb-content-title")})
    content_number=soup.find_all("li",attrs={"class":"board-thumb-content-number"})

    embed=discord.Embed(title=webTitle, url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srUpperNoticeYn=on&article.offset=0", icon_url="https://www.smu.ac.kr/favicon.ico", description="통합공지 조회", color=0x2e35ff)
    embed.set_author(name="상명대학교 알리미 슴우")
    embed.set_thumbnail(url="https://www.smu.ac.kr/favicon.ico")

    for i in range(10):

        title=content_titles[i].find_all("a")
        link="https://www.smu.ac.kr/lounge/notice/notice.do"+title[1]["href"]
        content_writer=content_number[i].next_sibling.next_sibling
        content_date=content_number[i].next_sibling.next_sibling.next_sibling.next_sibling
        date=content_date.get_text().split("\n")[2].strip()
        embed.add_field(name=str(i+1)+". `"+date+"`", value=str("["+title[1].get_text().strip()+"]("+link+")"), inline=False)
        print(title[1].get_text().strip())
        print(content_writer.get_text().split("\n")[2].strip())
        print(content_date.get_text().split("\n")[2].strip())
        print(link)

        embed.set_footer(text="1 페이지")
    await ctx.send(embed=embed)



bot.run(Token)#토큰 보안