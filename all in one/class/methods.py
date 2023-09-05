# __x__ şeklinde olan methodlara double under score (dunder) denir.
class Kitap:
    def __init__(self, isim, yazar, sayfa_sayisi, tür):
        print("İnit fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür

    def __str__(self):  # Bu fonksiyona yazdığımız şeyler, print ile döndürülür.
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(
            self.isim, self.yazar, self.sayfa_sayisi, self.tür
        )

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):  # Del'e ekstra özellik ekleniyor.
        print("Kitap Objesi Siliniyor...")

    def __repr__(
        self,
    ):  # Memory'de kaydedilen alan yerine yazılan kodu döndürülen dunder methodu.
        return "{} yazarının yazdığı {} isimli {} türü {} sayfası olan kitap sisteme kaydedilmiştir.".format(
            self.yazar, self.isim, self.tür, self.sayfa_sayisi
        )


kitap = Kitap("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")
print("1")
print(kitap)
print("2")
print(len(kitap))
print("3")
print(kitap.__dir__())  # dunder'leri ve methodları listeler.
print("4")
del kitap  # Kitap objesini sildi.
