class Calisan:
    def __init__(self, isim, maas, departman):
        print("Calisan Sınıfı init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print(
            """
        Çalışan Sınıfının Bilgileri

        İsim: {}
        Maas: {}
        Departman: {}        
        """.format(
                self.isim, self.maas, self.departman
            )
        )

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        super().__init__(isim, maas, departman)
        print("Yönetici Sınıfı İnit Fonksiyonu")
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self):
        print(
            """Yönetici Sınıfının Bilgileri
        İsim: {}
        Maaş: {}
        Departman: {}
        Sorumlu Kişi Sayısı: {}""".format(
                self.isim, self.maas, self.departman, self.kisi_sayisi
            )
        )

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari


yönetici = Yonetici("Thomas Shelby", 21000, "Bilişim", 100)
yönetici.bilgileri_goster()
