import requests
from bs4 import BeautifulSoup


fist = input("Enter a name of web site: ")

if fist == "Torrent new":
    CATEGORY="newgames"
    URL="https://itorrents-igruha.org/" + CATEGORY

    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")
    games = soup.find_all('div', class_="short-item22 rel-item22")

    for name in games:
        title = name.find('a', class_="act-item32").get_text()
        print(title)
else:
    print("no")


