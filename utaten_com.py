import requests

from bs4 import BeautifulSoup


response = requests.get("https://utaten.com/lyric/ma19042309/")
# エンコード
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

# 歌情報
# 曲名
kyokumei = soup.find("span", class_="movieTtl_mainTxt").string

info = soup.find_all("dd", class_="lyricWork__body")
# 作詞
sakusi = info[0].string
# 作曲
sakkyoku = info[1].string

# 歌詞
a = soup.find("div", class_="hiragana")

# ふりがな削除
for i in a.find_all("span", class_="rt"):
    i.extract()

text = f"""曲名:{kyokumei}
作詞:{sakusi}
作曲:{sakkyoku}
# ------------------ #
{a.text}"""
