import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h3")

with open("noticias.txt", "w") as file:
    for t in titles:
        file.write(t.text + "\n")

print("Notícias guardadas!")