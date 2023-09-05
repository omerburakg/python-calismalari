with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r+",
    encoding="utf-8",
) as file:
    icerik = file.read()
    icerik = "Ata Demirer\n" + icerik  # başa isim ekledik.
    file.seek(0)
    file.write(icerik)
