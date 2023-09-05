import os                 #anlatılan modül
from datetime import datetime

# print(os.listdir())        # os'un içinde bulunduğu klasördeki dosyaları sıralar
for i in os.listdir():
    print(i)


print(os.getcwd())         # os'un bulunduğu klasörü gösterir.
#os.mkdir("os_deneme1")     # os'un bulunduğu dizinde bir klasör oluşturur.
## os.chdir("C:\Users\omerb\Desktop")         os'un klasörünü değiştirir.    
#os.makedirs("os_deneme2/os_deneme3") # iç içe 2 klasör oluşturur.
#
#os.rmdir("os_deneme2/os_deneme3")  # deneme3 klasörünü silecektir.
#
#os.mkdir("os_deneme2/os_deneme3")  # deneme 3 klasörünü deneme2 klasörünün içinde oluşturacaktır.

#os.rmdir("os_deneme1")     # deneme1 klasörünü sildi.
#os.removedirs("os_deneme2/os_deneme3") # iki klasörü de silecektir.

#os.rename("test.txt","test_os.txt")   #os'un bulunduğu yerdeki şeylerin adını değiştirme.
#print(os.stat("test_os.txt"))
#print(os.stat("test_os.txt").st_mtime)     # değiştirilme zamanının saniye cinsinden karşılığına ulaştık.
#print(datetime.fromtimestamp(os.stat("test_os.txt").st_mtime))   # tarih olarak ayarlar.

for i in os.walk("C:/Users/omerb/Desktop"):     # os.walk("dizin") belirlenen dizinin altındaki her şeyi dolaşır.
    print(i)

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:/Users/omerb/Desktop"):     # os.walk("dizin") belirlenen dizinin altındaki her şeyi dolaşır.
    print("Klasör Yolu:",klasor_yolu)
    print("Klasör İsmi:",klasor_isimleri)
    print("Dosya İsmi:",dosya_isimleri)
    print("*********************************")
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print(i)