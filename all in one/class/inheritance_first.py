import datetime


class Person:
    def __init__(self, isim, telefon, dogum_tarihi):
        self.isim = isim
        self.telefon = telefon
        self.dogum_tarihi = dogum_tarihi

    def yas_hesaplama(self):
        guncel_tarih = datetime.datetime.now()
        guncel_yil = guncel_tarih.year
        yas = guncel_yil - self.dogum_tarihi
        return yas

    def bilgileri_goster(self):
        return """
        İsim: {}
        Telefon Numarası: {}   
        Doğum Tarihi: {}
        """.format(
            self.isim, self.telefon, self.dogum_tarihi
        )


class Ogrenci(Person):
    def __init__(self, isim, telefon, dogum_tarihi, ogrenci_numarasi, transkript):
        super().__init__(isim, telefon, dogum_tarihi)
        self.ogrenci_numarasi = ogrenci_numarasi
        self.transkript = transkript

    def not_ortalamasi(self):
        ort = 0
        for i in self.transkript:
            ort += i
        ort = ort / (len(self.transkript) + 1)
        return ort

    def bilgileri_goster(self):
        return """
        İsim: {}
        Telefon Numarası: {}   
        Doğum Tarihi: {}
        Öğrenci Numarası: {}
        Transkript: {}
        """.format(
            self.isim,
            self.telefon,
            self.dogum_tarihi,
            self.ogrenci_numarasi,
            self.transkript,
        )


class Ogretmen(Person):
    def __init__(self, isim, telefon, dogum_tarihi, maas):
        super().__init__(isim, telefon, dogum_tarihi)
        self.maas = maas

    def bilgileri_goster(self):
        return """
        İsim: {}
        Telefon Numarası: {}   
        Doğum Tarihi: {}
        Maaş: {} 
        """.format(
            self.isim, self.telefon, self.dogum_tarihi, self.maas
        )


öğrenci1 = Ogrenci(
    "Burak", "+906653233", 1999, 192808049, [10, 40, 50, 32, 50, 21, 53, 100, 78, 75]
)
öğretmen1 = Ogretmen("Ethem", "+90213123", 1975, 15000)
kişi1 = Person("Özgür", "+90213213", 2001)

print(kişi1.bilgileri_goster())
print(öğrenci1.bilgileri_goster())
print(öğrenci1.not_ortalamasi())
print(öğretmen1.bilgileri_goster())
