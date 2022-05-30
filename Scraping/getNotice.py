import requests
from bs4 import BeautifulSoup
import re
response = requests.get("https://www.smu.ac.kr/lounge/notice/notice.do?srUpperNoticeYn=on")
html=response.text
soup=BeautifulSoup(html,'lxml')
content_titles=soup.find_all("dt",attrs={"class":re.compile("^board-thumb-content-title")})
content_number=soup.find_all("li",attrs={"class":"board-thumb-content-number"})
for i in range(10):

    title=content_titles[i].find_all("a")
    link="https://www.smu.ac.kr/lounge/notice/notice.do"+title[1]["href"]
    content_writer=content_number[i].next_sibling.next_sibling
    content_date=content_number[i].next_sibling.next_sibling.next_sibling.next_sibling
    print(title[1].get_text().strip())
    print(content_writer.get_text().split("\n")[2].strip())
    print(content_date.get_text().split("\n")[2].strip())
    print(link)