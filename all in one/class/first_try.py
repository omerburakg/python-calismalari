class Ucus:
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure

    def anons_yap(self):
        return "{} sefer sayili {} - {} ucusumuz {} dakika sürecektir.".format(
            self.kod, self.kalkis, self.varis, self.sure
        )


ucus1 = Ucus("THK241", "IZM", "IST", "72")

print(ucus1.anons_yap())
