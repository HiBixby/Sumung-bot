import requests
from bs4 import BeautifulSoup
import re
import discord

def createEmbedNotice(page=1,articleLimit=5):
    page=max(1,abs(page))
    articleLimit=min(10,abs(articleLimit))
    articleOffset=(page-1)*articleLimit
    url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit="+str(articleLimit)+"&srUpperNoticeYn=on&article.offset="+str(articleOffset)

    response = requests.get(url,verify=False)
    html=response.text

    soup=BeautifulSoup(html,'lxml')

    webTitle=soup.find("title").get_text() #<title>태그 내용

    content_titles=soup.find_all("dt",attrs={"class":re.compile("^board-thumb-content-title")})
    content_number=soup.find_all("li",attrs={"class":"board-thumb-content-number"})

    embed=discord.Embed(title=webTitle, url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srUpperNoticeYn=on&article.offset=0", description="통합공지 "+str(articleLimit)+"개씩 보기", color=0xFFD9B5)
    embed.set_author(name="📢 상명대학교 공지사항") #임베드 맨 윗줄 Aauthor
    #embed.set_thumbnail(url="https://www.smu.ac.kr/favicon.ico") #임베드 썸네일
    numberEmoji=["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

    for i in range(articleLimit):
        title=content_titles[i].find_all("a")
        link="https://www.smu.ac.kr/lounge/notice/notice.do"+title[1]["href"] #i번째 공지사항 링크
        content_writer=content_number[i].next_sibling.next_sibling
        content_date=content_number[i].next_sibling.next_sibling.next_sibling.next_sibling

        date=content_date.get_text().split("\n")[2].strip()
        cmp,cate=title[0].get_text().strip().split("\n")

        name=numberEmoji[i+1]+" "+cmp+" "+cate
        value=str("["+title[1].get_text().strip()+"]("+link+")"+" `"+date+"`")
        embed.add_field(name=name, value=value, inline=False)
        
        '''
        print(title[1].get_text().strip())
        print(content_writer.get_text().split("\n")[2].strip())
        print(content_date.get_text().split("\n")[2].strip())
        print(link)
        '''
    embed.set_footer(text=str(page)+" 페이지")
    return embed