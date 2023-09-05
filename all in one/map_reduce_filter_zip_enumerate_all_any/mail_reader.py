# Problem 3
# Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
#
#                     coskun.m.murat@gmail.com
#                     example@xyz.com
#                     mustafa.com
#                     mustafa@gmail
#                     kerim@yahoo.com
#
#                            //
#                            //
#                            //
#
#
# *İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*

file = open("mailler.txt", "r", encoding="utf-8")
for satir in file:
    satir = satir[:-1]
    if (satir.endswith(".com")) and (satir.find("@") != -1):
        print(satir)
