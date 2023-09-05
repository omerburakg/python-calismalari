import sqlite3

con = sqlite3.connect("kütüphane.db")  # db bağlanır. Bu isimde db yoksa db oluşturur.

cursor = con.cursor()  # İmleç Oluşturur.


def tablo_olustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,Yazar TEXT,Yayınevi TEXT, Sayfa_sayısı INT)"
    )
    # veritabanında yoksa oluşturacak.
    con.commit()
    # Bunu yapmazsak çalışmaz.


def veri_ekle():
    cursor.execute(
        "Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)"
    )
    # tabloya veri eklemek.
    con.commit()


def veri_ekle2(isim, yazar, yayınevi, sayfa_sayisi):
    cursor.execute(
        "Insert into kitaplık Values(?,?,?,?)", (isim, yazar, yayınevi, sayfa_sayisi)
    )  # ? işareti yerine sırasıyla gelir.
    con.commit()


def verileri_al():  # tüm verileri çekme
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)


def verileri_al2():  # sadece isim ve yazar verilerini çekme
    cursor.execute("Select isim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)


def verileri_al3(
    yayınevi,
):  # yayınevi girip ona göre veri almak.  verileri_al3("Everest")
    cursor.execute("Select * From kitaplık where Yayınevi =?", (yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)


def verileri_guncelle(
    eski_yayınevi, yeni_yayınevi
):  # veri güncelleme yayınevi için. verileri_guncelle("Doğan Kitap","Everest")
    cursor.execute(
        "Update kitaplık set Yayınevi = ? where Yayınevi = ?",
        (yeni_yayınevi, eski_yayınevi),
    )
    con.commit()


def verileri_sil(yazar):  # yazara göre veri silme  verileri_sil("Ahmet Ümit")
    cursor.execute("Delete from kitaplık where Yazar = ? ", (yazar,))
    con.commit()


# isim = input("İsim: ")
# yazar = input("Yazar: ")
# yayınevi = input("Yayınevi: ")
# sayfa_sayisi = int(input("Sayfa Sayısı: "))

con.close()  # connection'u kapatır. Dosya işlemlerindeki gibi bunu kapatmalıyız.
