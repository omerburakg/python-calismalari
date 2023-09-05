class Yazilimci:
    def __init__(self, isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def bilgileri_goster(self):
        print(
            """
        Yazılımcı Objesinin Özellikleri

        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}        
        """.format(
                self.isim, self.soyisim, self.numara, self.maas, self.diller
            )
        )

    def zam_yap(self, zam_miktari):
        print("Zam Yapıldı!")
        self.maas += zam_miktari

    def dil_ekle(self, yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)


yazilimci1 = Yazilimci("Omer", "Burak", "0555555555", 3000, ["Python", "C", "Js"])
yazilimci1.bilgileri_goster()
yazilimci1.dil_ekle("Kotlin")
yazilimci1.bilgileri_goster()
yazilimci1.zam_yap(1250)
yazilimci1.bilgileri_goster()
