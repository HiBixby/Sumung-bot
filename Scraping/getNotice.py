import requests
from bs4 import BeautifulSoup
import re
from Discord import embedMessage
import discord

response = requests.get("https://www.smu.ac.kr/lounge/notice/notice.do?srUpperNoticeYn=on")
html=response.text
soup=BeautifulSoup(html,'lxml')

webTitle=soup.find("title").get_text()

content_titles=soup.find_all("dt",attrs={"class":re.compile("^board-thumb-content-title")})
content_number=soup.find_all("li",attrs={"class":"board-thumb-content-number"})

embed=discord.Embed(title="상명라운지 | 통합공지 게시판목록 | 상명라운지", url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srUpperNoticeYn=on&article.offset=0",icon_url="https://www.smu.ac.kr/favicon.ico", description="통합공지 조회", color=0x2e35ff)
embed.set_author(name="상명대학교 알리미 슴우")
embed.set_thumbnail(url="https://www.smu.ac.kr/favicon.ico")

for i in range(10):

    title=content_titles[i].find_all("a")
    link="https://www.smu.ac.kr/lounge/notice/notice.do"+title[1]["href"]
    content_writer=content_number[i].next_sibling.next_sibling
    content_date=content_number[i].next_sibling.next_sibling.next_sibling.next_sibling
    embed.add_field(name=[title[1].get_text().strip()](link), value="undefined", inline=False)
    print(title[1].get_text().strip())
    print(content_writer.get_text().split("\n")[2].strip())
    print(content_date.get_text().split("\n")[2].strip())
    print(link)

    embed.set_footer(text="1 페이지")

def CreateNoticeEmbed(embed):
    return embed