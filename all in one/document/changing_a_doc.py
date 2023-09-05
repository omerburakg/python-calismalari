with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r+",
    encoding="utf-8",
) as file:
    file.seek(10)
    file.write("Deneme")
    file.seek(0)
    print(file.read())
