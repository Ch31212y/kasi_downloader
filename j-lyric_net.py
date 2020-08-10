import requests

from bs4 import BeautifulSoup


response = requests.get("https://j-lyric.net/artist/a04cc4b/l00bb39.html")
# エンコード
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

# 曲の情報があるところ取得
rea = soup.find("div", class_="lbdy")

# 曲の詳細
info = rea.find_all("p", attrs={"class": "sml"})
# 歌い手
singer = info[0].find("a").string
# 作詞：
sakusi = info[1].string
# 作曲：
sakkyoku = info[2].string

# 歌詞抽出
kasi = rea.find("p", attrs={"id": "Lyric"})
# brを改行にする
for i in kasi.select("br"):
    i.replace_with("\n")

text = f"""歌い手: {singer}
作詞: {sakusi}
作曲: {sakkyoku}
# ------------------------------- #
{kasi.text.replace("　", " ")}"""
