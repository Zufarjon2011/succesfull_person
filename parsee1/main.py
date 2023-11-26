import requests
from bs4 import BeautifulSoup

CATEGORY="society"
URL="https://www.gazeta.uz/ru/" + CATEGORY

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

html = requests.get(URL, headers=HEADER).text
soup = BeautifulSoup(html, "html.parser")
Block = soup.find_all('div', class_="nblock")

for news in Block:
    title = news.find('div', class_="nt").find("h3").get_text(strip=True)
    pub = news.find('div',class_="ndt").get_text()
    desc = news.find("p").get_text()
    print(title + "     " +desc + "         " + pub )



