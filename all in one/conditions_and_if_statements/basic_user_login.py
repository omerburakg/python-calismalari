print(
    """********************************************
            KULLANICI GIRISI
********************************************"""
)

sys_kullanici_adi = "bburak"
sys_sifre = "12345"

kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Sifreyi Giriniz: ")

if sys_kullanici_adi == kullanici_adi and sys_sifre == sifre:
    print("Giriş Başarılı. Yönlendiriliyor........")
elif sys_kullanici_adi == kullanici_adi and sys_sifre != sifre:
    print("Parola Hatalı!")
elif sys_kullanici_adi != kullanici_adi or sys_sifre != sifre:
    print("Kullanıcı adı ya da parola hatalı!")
else:
    print("Bir Hata Meydana Geldi.")
