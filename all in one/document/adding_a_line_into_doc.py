with open(
    "C:/Users/omerb/Desktop/well well well/projeler/kodlama_egzersizleri/document/bilgiler.txt",
    "r+",
    encoding="utf-8",
) as file:
    liste = file.readlines()
    liste.insert(3, "Necip Aydın\n")
    file.seek(0)
    file.writelines(liste)
    file.seek(0)
    print(file.read())


#  for i in liste:             diğer şekilde böyle ekleyebilirdik.
#        file.write(i)
