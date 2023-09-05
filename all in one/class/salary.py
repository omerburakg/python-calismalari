class Account:
    def __init__(self, banka, kurum, maas, izin):
        self.banka = banka
        self.kurum = kurum
        self.__maas = maas  # private
        self.izin = izin

    izin = 14
    kurum = "sgk"
    __maas = 8500
    banka = "is"

    def getMaas(self):
        return self.__maas

    def arttirMaas(self, artis):
        self.__maas += artis
        return self.__maas

    def azaltMaas(self, azaltma):
        self.__maas -= azaltma
        return self.__maas


class Ogretmen(Account):
    def __init__(self, banka, kurum, maas, izin, okul, ogretmen_id):
        super().__init__(banka, kurum, maas, izin)
        self.okul = okul
        self.__ogretmen_id = ogretmen_id

    def getId(self):
        return self.__ogretmen_id

    def getSchool(self):
        return self.okul


class Isci(Account):
    def __init__(self, banka, kurum, maas, izin, alan, isci_id):
        super().__init__(banka, kurum, maas, izin)
        self.alan = alan
        self.__isci_id = isci_id

    def getId(self):
        return self.__isci_id


herhangi = Account("ziraat", "bagkur", 8500, 18)
o1 = Ogretmen("is", "sgk", 12000, 21, "Atatürk İlköğretim Okulu", 192084908)
i1 = Isci("akbank", "bagkur", 10000, 14, "maden", 23819238)
print("\n")
print(o1.getId())
print(i1.getId())

o1.arttirMaas(2200)
print(o1.getMaas())
