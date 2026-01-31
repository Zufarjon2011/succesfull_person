# # import requests
# # from bs4 import BeautifulSoup
# #
# # CATEGORY="society"
# # URL="https://www.gazeta.uz/ru/" + CATEGORY
# #
# # HEADER = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# # }
# #
# # html = requests.get(URL, headers=HEADER).text
# # soup = BeautifulSoup(html, "html.parser")
# # Block = soup.find_all('div', class_="nblock")
# #
# # for news in Block:
# #     title = news.find('div', class_="nt").find("h3").get_text(strip=True)
# #     print(title)
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # CATEGORY="politics"
# # URL="https://www.gazeta.uz/ru/" + CATEGORY
# #
# # HEADER = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# # }
# #
# # html = requests.get(URL, headers=HEADER).text
# # soup = BeautifulSoup(html, "html.parser")
# # Block = soup.find_all('div', class_="nblock")
# #
# # for el in Block:
# #     title = el.find('div', class_="nt").find("h3").get_text(strip=True)
# #     title2 =
# #     print(title)
#
# import requests
# from bs4 import BeautifulSoup
#
# URL="https://www.afisha.uz/ru"
#
# HEADER = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# }
#
# html = requests.get(URL)
# # soup = BeautifulSoup(html, "html.parser")
# # Block = soup.find_all('li', class_="md:p-3.5 md:hover:bg-gray-100 md:rounded-md")
# #
# # for el in Block:
# #     title = el.find('div', class_="relative flex-1 overflow-hidden md:order-last").find("h3").get_text()
# #     print(title)

import requests
from bs4 import BeautifulSoup

CATEGORY="top10-online.html"
URL="https://itorrents-igruha.org/" + CATEGORY

html = requests.get(URL)
soup = BeautifulSoup(html, "html.parser")
Block = soup.find_all('div', class_="short-item22 rel-item22")

for el in Block:
    title = el.find

