# Problem 1
# Elinizde uzunca bir string olsun.

#            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


# Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

# *İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.*#

x = input("Kelimeyi Giriniz: ")

sayi_sozluk = dict()

for harf in x:
    if harf in sayi_sozluk:
        sayi_sozluk[harf] += 1
    else:
        sayi_sozluk[harf] = 1
for i, j in sayi_sozluk.items():
    print(i, ":", j)
