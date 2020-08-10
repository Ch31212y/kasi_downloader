import requests

from bs4 import BeautifulSoup


response = requests.get("https://www.utamap.com/showtop.php?surl=65571")
# エンコード
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

uta = soup.find("td", class_="kasi_border")

kyokumei = uta.find("td", class_="kasi1")
info = uta.find_all("td", class_="pad5x10x0x10")

sakusi = info[1].string
sakkyoku = info[3].string
utaite = info[5].string

kasi = uta.find("td", class_="noprint kasi_honbun")
for i in kasi.select("br"):
    i.replace_with("\n")
print(kasi.text)

text = f"""曲名:{kyokumei}
作詞:{sakusi}
作曲:{sakkyoku}
# ------------------ #
{kasi.text}"""
