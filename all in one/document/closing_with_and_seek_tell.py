with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
) as file:
    for i in file:
        print(i)
# İşlem tamamlandıktan sonra dosya kapanır.


with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
) as file:
    file.seek(5)  # 5. Byte'a gitti.
    icerik = file.read(10)  # 10 karakter okuttuk.
    print(file.tell())  # Kaçıncı byte'da olduğumuzu döndürür
    file.seek(0)  # 0'a döndürdük.
    icerik2 = file.read(6)  # 6 karakter okuttuk.
    print(file.tell())
    print(icerik)
    print(icerik2)
