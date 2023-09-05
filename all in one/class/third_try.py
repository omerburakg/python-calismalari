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
    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari
        print("Zam Yapıldı.")


yönetici = Yonetici("Burak", 10000, "Bilişim")

yönetici.zam_yap(1200)

yönetici.bilgileri_goster()
