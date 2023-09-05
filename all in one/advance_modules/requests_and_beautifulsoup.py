import requests
from bs4 import BeautifulSoup            #html veri çeker. dinamik js görünce patlıyo pü

# ABANDONED LAZIMSA SELENIUM OGREN GG


url = "https://yellowpages.com.tr/ara?q=ankara"
response = requests.get(url)             #bilgi çekme

# print(response) çekip çekmediğini görmek için kontrol

html_icerigi = response.content   #sayfa kaynagı

soup = BeautifulSoup(html_icerigi,"html.parser")         #parcalamak icin

# print(soup.prettify())             #çekilen bilgileri düzenleyip html formatında almak için

# print(soup.find_all("a"))

for i in soup.find_all("a"):         # html içinde <a> etiketini aratma
    print(i.get("href"))             # a etiketi içindeki href etiketlerini almak
    print("****************************")