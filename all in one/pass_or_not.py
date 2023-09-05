kalanlar = []
gecenler = []


def not_hesaplama(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    ort = (not1 * (3 / 10)) + (not2 * (3 / 10)) + (not3 * (4 / 10))
    if ort >= 90:
        harf = "AA"
    elif ort >= 85:
        harf = "BA"
    elif ort >= 80:
        harf = "BB"
    elif ort >= 75:
        harf = "CB"
    elif ort >= 70:
        harf = "CC"
    elif ort >= 65:
        harf = "DC"
    elif ort >= 60:
        harf = "DD"
    elif ort >= 55:
        harf = "FD"
    else:
        harf = "FF"
    if harf == "FF" or harf == "FD":
        kalanlar.append(isim + "-------------> " + harf + "\n")
    else:
        gecenler.append(isim + "-------------> " + harf + "\n")


with open("students.txt", "r", encoding="utf-8") as file:
    file.seek(0)
    for i in file:
        not_hesaplama(i)
with open("gecenler.txt", "w+", encoding="utf8") as gecenlerfile:
    for x in gecenler:
        gecenlerfile.write(x)
with open("kalanlar.txt", "w+", encoding="utf-8") as kalanlarfile:
    for y in kalanlar:
        kalanlarfile.write(y)
