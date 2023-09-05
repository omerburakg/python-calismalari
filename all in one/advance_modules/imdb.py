import requests
from bs4 import BeautifulSoup


a = float(input("Rating'i giriniz: "))

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)     # [200]

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("td",{"class":"titleColumn"})    #class'ı titleColumn olan td etiketini çekme
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})         #ratingColumn imdbRating çekme

for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
    if float(rating) >= a:
        print("Film Adı:",baslik)
        print("Film Rating:",rating)
