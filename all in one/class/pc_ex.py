import random
import time


class Bilgisayar:
    def __init__(
        self,
        pc_durumu="Kapali",
        uygulamalar=[
            "Word",
            "VSCode",
            "Chrome",
            "SOLIDWORKS",
            "CATIA",
            "AUTOCAD",
            "PyCharm",
        ],
        ses=20,
        parlaklik=100,
        acik_uygulama="VSCode",
    ):
        self.pc_durumu = pc_durumu
        self.uygulamalar = uygulamalar
        self.ses = ses
        self.parlaklik = parlaklik
        self.acik_uygulama = acik_uygulama

    def pc_kapat(self):
        if self.pc_durumu == "Kapali":
            print("Bilgisayar Zaten Kapali..")
        elif self.pc_durumu != "Kapali":
            print("Bilgisayar Kapatiliyor...")
            self.pc_durumu = "Kapali"

    def pc_ac(self):
        if self.pc_durumu == "Acik":
            print("Bilgisayar Zaten Acik..")
        elif self.pc_durumu != "Acik":
            print("Bilgisayar Aciliyor...")
            self.pc_durumu = "Acik"

    def uygulama_ekleme(self, uygulamalar):
        self.uygulamalar.append(uygulamalar)

    def uygulama_cikarma(self, uygulama):
        self.uygulamalar.remove(uygulama)
        return self.uygulamalar

    def ses_ac(self):
        if self.ses < 100:
            self.ses += 1
            print("Ses Seviyesi:", self.ses)
        else:
            print("Ses:", self.ses)

    def ses_kis(self):
        if self.ses > 0:
            self.ses -= 1
            print("Ses Seviyesi:", self.ses)
        else:
            print("Ses:", self.ses)

    def parlaklik_arttir(self):
        if self.parlaklik < 100:
            self.parlaklik += 5
            print("Parlaklik Seviyesi:", self.parlaklik)
        else:
            print("Parlaklik:", self.parlaklik)

    def parlaklik_kis(self):
        if self.parlaklik > 0:
            self.parlaklik -= 5
            print("Parlaklik Seviyesi:", self.parlaklik)
        else:
            print("Parlaklik:", self.parlaklik)

    def rastgele_uygulama(self):
        rastgele = random.randint(0, len(self.uygulamalar) - 1)
        self.acik_uygulama = self.uygulamalar[rastgele]
        print("Acilan Uygulama:", self.acik_uygulama)

    def uygulama_ac(self):
        kelime = input("Aradiginiz Kelimeyi Tam İsmiyle ve Boşluk Birakmadan Giriniz: ")
        for i in self.uygulamalar:
            if kelime == i:
                print("Uygulama Araniyor...")
                self.acik_uygulama = i
                time.sleep(1)
                print("Uygulama Bulundu. Acik olan uygulama:", self.acik_uygulama)

    def __len__(self):
        return len(self.uygulamalar)

    def __str__(self):
        return "Pc Durumu: {} Uygulamalar: {} Ses: {} Parlaklik: {} Acik Uygulama: {}".format(
            self.pc_durumu,
            self.uygulamalar,
            self.ses,
            self.parlaklik,
            self.acik_uygulama,
        )


bilgisayar1 = Bilgisayar()
print(
    """
    BILGISAYAR ORNEGI
    1- PC AÇ
    2- PC KAPAT
    3- SES AYARLARI
    4- PARLAKLIK AYARLARI
    5- UYGULAMALAR
    6- UYGULAMA YUKLE
    7- RASTGELE UYGULAMA AÇ
    8- UYGULAMA AÇ
    9- PC DURUMU
    """
)
while True:
    islem = input("İşlemi Seçiniz: ")
    if islem == "1":
        bilgisayar1.pc_ac()
    elif islem == "2":
        bilgisayar1.pc_kapat()
    elif islem == "3":
        print("Ses Açmak İçin ' + ' Kismak Icin '-' Cikmak İcin 'q'")
        while True:
            x = input("İslem: ")
            if x == "+":
                bilgisayar1.ses_ac()
            elif x == "-":
                bilgisayar1.ses_kis()
            else:
                print("Ses: ", bilgisayar1.ses)
                break
    elif islem == "4":
        print("Parlaklik Arttirmak İcin '+' Azaltmak İcin '-' Cikmak İcin 'q'")
        while True:
            x = input("İslem: ")
            if x == "+":
                bilgisayar1.parlaklik_arttir()
            elif x == "-":
                bilgisayar1.parlaklik_kis()
            else:
                print("Parlaklik Seviyesi: ", bilgisayar1.parlaklik)
                break
    elif islem == "5":
        print(bilgisayar1.uygulamalar)
    elif islem == "6":
        uygulama_isimleri = input("Kanal İsimlerini ' , ' ile ayirarak giriniz: ")
        uygulama_listesi = uygulama_isimleri.split(",")
        for i in uygulama_listesi:
            bilgisayar1.uygulama_ekleme(i)
    elif islem == "7":
        bilgisayar1.rastgele_uygulama()
    elif islem == "8":
        bilgisayar1.uygulama_ac()
    elif islem == "9":
        print(bilgisayar1)
    else:
        print("Geçersiz Bir İşlem Girdiniz!")
