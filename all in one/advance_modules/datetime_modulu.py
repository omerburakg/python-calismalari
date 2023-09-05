from datetime import datetime               #Önemli olan kısım burası
import locale                               # Gün ve Ay isimlerini türkçe yapmak ve bölgenin Türkiye olduğunu belirlemek için locale modülü kullanılır.
import os
import time

locale.setlocale(locale.LC_ALL,"")          # Tr ayarlaması
# datetime modülü ile anlık saati ve birçok şeyi kullanabiliriz.
# YY-AA-GG        HH-MM
su_an = datetime.now()

yıl = su_an.year

ay = su_an.month

saat = su_an.hour
dakika = su_an.minute
print("\nprint(yıl,ay,saat,dakika)")
print(yıl,ay,saat,dakika)


time.sleep(4)
os.system('cls')
##########################################
print("print(datetime.ctime(su_an))\n")
print(datetime.ctime(su_an))           #anlık saati içeri gönderdiğimizde daha güzel bir gösterim ile geri döndürür.


time.sleep(4)
os.system('cls')

##########################################
"""
strftime() fonksiyonu

Yıl bilgisini almak için: %Y
Ay ismini almak için: %B
Gün ismini almak için: %A
Saat bilgisini almak için: %X
Gün bilgisini almak için: %D

"""
print('print(datetime.strftime(su_an,"%B %Y" &A))\n')
print(datetime.strftime(su_an,"%B %Y %A"))

time.sleep(4)
os.system('cls')

##########################################
"su anki zamanın saniye cinsindeki hali .timestamp()"

saniye = datetime.timestamp(su_an)
print("Saniye:",saniye)

"saniyeyi su anki zamana döndürme"
su_an2 = datetime.fromtimestamp(saniye)

print(su_an2)

time.sleep(4)
os.system("cls")

# print(datetime.fromtimestamp(0))        Bilgisayarlarda milad 1970-01-01 03.00 olarak alınmıştır. İşlemler buna göre yapılır.

##########################################
"basit bir örnek:"

tarih = datetime(1999,10,8)

simdi = datetime.now()

print("Fark:",simdi-tarih)