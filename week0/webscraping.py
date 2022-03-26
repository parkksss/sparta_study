import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in musics:
    title_temp = music.select_one('td.info > a.title.ellipsis')
    not_title = music.select_one('.icon-19')
    if not_title is not None:
        title_temp.span.decompose()

    title = title_temp.text.strip()   # strip() : 앞,뒤 여백 자르기
    artist = music.select_one('td.info > a.artist.ellipsis').text
    rank = music.select_one('td.number').text[0:2].strip()    # text[0:2] : 앞에서 두 글자만 끊기

    print(rank, title, artist)