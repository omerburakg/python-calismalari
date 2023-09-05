import sqlite3

con = sqlite3.connect("kütüphane.db")   #db bağlanır. Bu isimde db yoksa oluşturur.

cursor = con.cursor()   #imleç oluşturma

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayısı INT)")
    #veritabanında sorgulama yapıp oluşturacak.
    con.commit()
    # bunu yapmazsak çalışmaz ve sorgulamaz.
def veri_ekle():
    cursor.execute("Insert into kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)"(isim,yazar,yayınevi,sayfa_sayisi))
    con.commit()
isim = input("İsim:" )
yazar = input("Yazar: ")
yayınevi = input("Yayınevi: ")
sayfa_sayisi = int(input("Sayfa Sayısı: "))
veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi)
con.close()  # dosya işlemleri gibi bittiğinde kapatılmalıdır.
