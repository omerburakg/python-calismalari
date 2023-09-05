with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r+",
    encoding="UTF-8",
) as file:
    file.seek(10)
    file.write("Deneme")
with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r+",
    encoding="UTF-8",
) as file:
    print(file.read())
