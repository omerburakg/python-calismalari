datas = {
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "bes",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz",
    0: "sıfır",
}
phone = input("Telefon numaranızı basında 0 olmadan giriniz: ")
char = 0

for i in phone:
    print(datas.get(int(i)))
