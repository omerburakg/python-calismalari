class Animal:
    def __init__(self, beslenme, icgüdü, yavru_sayisi):
        self.beslenme = beslenme
        self.icgüdü = icgüdü
        self.yavru_sayisi = yavru_sayisi


class Kopek(Animal):
    def __init__(self, beslenme, icgüdü, yavru_sayisi, cikardigi_ses, ayak_sayisi):
        super().__init__(beslenme, icgüdü, yavru_sayisi)
        self.cikardigi_ses = cikardigi_ses
        self.ayak_sayisi = ayak_sayisi

    def __len__(self):
        return self.ayak_sayisi

    def __str__(self):
        return "KÖPEK OZELIKLERI\nBeslenme: {} İcgüdü: {} Yavru Sayısı: {} Cikardigi Ses: {} Ayak Sayisi:{}".format(
            self.beslenme,
            self.icgüdü,
            self.yavru_sayisi,
            self.cikardigi_ses,
            self.ayak_sayisi,
        )


class Kus(Animal):
    def __init__(
        self, beslenme, icgüdü, yavru_sayisi, ucma, cikardigi_ses, ayak_sayisi
    ):
        super().__init__(beslenme, icgüdü, yavru_sayisi)
        self.ucma = ucma
        self.ayak_sayisi = ayak_sayisi
        self.cikardigi_ses = cikardigi_ses

    def __len__(self):
        return self.ayak_sayisi

    def __str__(self):
        return "KUS OZELLIKLERI\n Beslenme: {} İcgüdü: {} Yavru Sayisi: {} Cikardigi Ses: {} Ayak Sayisi: {}".format(
            self.beslenme,
            self.icgüdü,
            self.yavru_sayisi,
            self.cikardigi_ses,
            self.ayak_sayisi,
        )


class At(Animal):
    def __init__(
        self, beslenme, icgüdü, yavru_sayisi, boy, tür, ayak_sayisi, cikardigi_ses
    ):
        super().__init__(beslenme, icgüdü, yavru_sayisi)
        self.boy = boy
        self.tür = tür
        self.ayak_sayisi = ayak_sayisi
        self.cikardigi_ses = cikardigi_ses

    def __len__(self):
        return self.ayak_sayisi

    def __str__(self):
        return "AT OZELLIKLERI\n Beslenme: {} İcgüdü: {} Yavru Sayisi: {} Boy: {} Tür: {} Cikardigi Ses: {} Ayak Sayisi: {}".format(
            self.beslenme,
            self.icgüdü,
            self.yavru_sayisi,
            self.boy,
            self.tür,
            self.cikardigi_ses,
            self.ayak_sayisi,
        )


köpke = Kopek("Etcil", "Refleksif/Evcilmen", 4, "Woof Woof", 4)
kus = Kus("Tohum ve Yem", "Refleksif/Doğal", 6, "UCAR", "Chirp Chirp!", 2)
at = At("Yem", "İcgüdüsel", 1, 185, "Yaris", "Neigh!", 4)

print(
    """
1- KOPKE OZELLIKLERI
2- KUS OZELLIKLERI
3- AT OZELLIKLERI

Cikmak icin 'q'
"""
)

while True:
    x = input("İşlemi Seçiniz: ")
    if x == "q":
        print("Cikis Yapiliyor...")
        break
    if x == "1":
        print(köpke)
    elif x == "2":
        print(kus)
    elif x == "3":
        print(at)
    else:
        print("Hatali İslem")
