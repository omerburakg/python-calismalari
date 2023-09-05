import random
import time


class Kumanda:
    def __init__(
        self, tv_durumu="Kapali", tv_ses=0, kanal_listesi=["TRT"], kanal="TRT"
    ):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durumu == "Acik":
            print("Televizyon Zaten Acik...")
        else:
            print("Televizyon Aciliyor...")
            self.tv_durumu = "Acik"

    def tv_kapat(self):
        if self.tv_durumu == "Kapali":
            print("Televizyon Zaten Kapali...")
        else:
            print("Televizyon Kapatiliyor...")
            self.tv_durumu = "Kapali"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttir: '>'\nCikis: 'cikis'")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses: {}".format(self.tv_ses))
            elif cevap == ">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def search(self):
        kelime = input("Aradiginiz Kanali Tam İsmiyle ve Boşluk Birakmadan Giriniz: ")
        for i in self.kanal_listesi:
            if kelime == i:
                print("Kanal Açiliyor...")
                time.sleep(1)
                self.kanal = kelime
                print("Şu Anki Kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return (
            "TV Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}\n".format(
                self.tv_durumu, self.tv_ses, self.kanal_listesi, self.kanal
            )
        )


kumanda = Kumanda()
print(
    """
Televizyon Uygulamasi
1- TV AÇ
2- TV KAPAT
3- SES AYARLARI
4- KANAL EKLE
5- KANAL SAYISI ÖĞRENME
6- RASTGELE KANAL
7- TELEVİZYON BİLGİLERİ
8- KANAL SEÇME
Cikis icin 'q' basiniz.
"""
)

while True:
    islem = input("İslemi seciniz: ")
    if islem == "q":
        time.sleep(1)
        print("Program Sonlaniyor...")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal İsimlerini ' , ' ile ayirarak giriniz: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        print("Kanal Sayisi:", len(kumanda))
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    elif islem == "8":
        kumanda.search()
    else:
        print("Geçersiz İşlem!")
