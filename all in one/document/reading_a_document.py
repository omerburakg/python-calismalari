file = open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
)

for i in file:
    print(i, end="")  # \n karakterini kaldırdık.
file.close()

file = open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
)
icerik = file.read()

print("Dosyanın İçeriği: ")
print(icerik)

print("Dosyanin İcerigi2: ")
icerik2 = file.read()  # Dosyanın geri kalanında bir şey olmadığı için boş kaldı.
print(icerik2)
file.close()

file = open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
)
print(file.readline())  # Satır satır dosyayı okur.
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print("--------")
print(file.readline())
file.close()


file = open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r",
    encoding="UTF-8",
)
liste = file.readlines()
print(liste)
file.close()
