#https://cog-creators.github.io/discord-embed-sandbox/
import discord

def CreateNoticeEmbed():
    embed=discord.Embed(title="상명라운지 | 통합공지 게시판목록 | 상명라운지", url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srUpperNoticeYn=on&article.offset=0",icon_url="https://www.smu.ac.kr/favicon.ico", description="통합공지 조회", color=0x2e35ff)
    embed.set_author(name="상명대학교 알리미 슴우")
    embed.set_thumbnail(url="https://www.smu.ac.kr/favicon.ico")
    embed.add_field(name="undefined", value="undefined", inline=False)
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
    return embed