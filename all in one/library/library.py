class Book:
    def __init__(self, name, page, author):
        self.name = name
        self.page = page
        self.author = author

    def __str__(self):
        return "{} {} {} sayfa".format(self.name, self.author, self.page)


class Library:
    def __init__(self):
        self.liste = []

    def add_book(self):
        name = input("Kitap Adı: ")
        author = input("Yazar Adı: ")
        page = input("Sayfa Sayısı: ")
        book = Book(name, page, author)
        self.liste.append(book)
        print(book.name, "isimli kitap sisteme eklendi.\n")

    def remove_book(self):
        name = input("Silmek istediğiniz kitabın adını giriniz: ")
        for i in self.liste:
            if i.name.lower() == name.lower():
                self.liste.remove(i)
                print(name, "isimli kitap sistemden silindi.\n")
                break
        else:
            print(name, "isimli kitap sistemde bulunamadı.")

    def list_book(self):
        print("Sisteme kayıtlı kitaplar: ")
        for i in self.liste:
            print(i)

    def run(self):
        while True:
            print("1- Kitap Ekle")
            print("2- Kitap Sil")
            print("3- Kitapları Görüntüle")
            print("4- Çıkış")
            secim = input("Seçiminizi Girin 1/2/3/4 : ")
            if secim == "1":
                self.add_book()
            elif secim == "2":
                self.remove_book()
            elif secim == "3":
                self.list_book()
            elif secim == "4":
                print("\nProgram sonlandırılıyor...\n")
                break
            else:
                print("\nGeçersiz işlem.\n")


library = Library()
library.run()
