class Book:
    def __init__(self,yazar,kitap_adi,sayfa,yayinevi):
        self.yazar = yazar
        self.kitap_adi = kitap_adi
        self.sayfa = sayfa
        self.yayinevi = yayinevi
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nYayınevi: {} ".format(self.kitap_adi,self.yazar,self.sayfa,self.yayinevi)
    def __len__(self):
        return self.sayfa
    
class Library:
    def __init__(self):
        self.liste = []
    
    def kitap_ekle(self):
        isim = input("Kitap adını giriniz: ")
        yazar = input("Yazar adını giriniz: ")
        sayfa = input("Kitabın sayfa sayısını giriniz: ")
        yayinevi = input("Yayınevini giriniz: ")    
        book = Book(yazar,isim,sayfa,yayinevi)
        self.liste.append(book)
    
    def kitap_sil(self):
        silinecek_kitap_adi = input("Silmek istediğiniz kitabın adını giriniz: ")
        for i in self.liste:
            if i.kitap_adi.lower() == silinecek_kitap_adi.lower():
                self.liste.remove(i)
                print("Kitap listeden silindi.")
                break
            else:
                print(silinecek_kitap_adi,"isimli bir kitap bulunmamaktadır.")
    def kitaplari_listele(self):
        for i in self.liste:
            print(i)
    
    def calistir(self):
        while True:
            x = input("Kitap Eklemek için 1, Kitap Silmek için 2, Kitap listelemek için 3, çıkmak için 4.\nSecimi giriniz: ")
            if x == "1":
                self.kitap_ekle()
            elif x == "2":
                self.kitap_sil()
            elif x == "3":
                self.kitaplari_listele()
            elif x == "4":
                print("finish.")
                break
            else:
                print("Geçersiz İşlem")

k = Library()
k.calistir()


