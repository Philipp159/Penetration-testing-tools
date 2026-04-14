import requests
from bs4 import BeautifulSoup

url = "https://example.com"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))
