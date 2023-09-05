print(
    """
*******************************************
            KULLANICI GİRİŞİ
*******************************************
"""
)

sys_kullanici_adi = "burak"
sys_pass = "12345"
deneme_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if parola == sys_pass and sys_kullanici_adi == kullanici_adi:
        print("Giriş Başarılı. Yönlendiriliyor...")
        break
    if deneme_hakki == 0:
        print("Çok Fazla Giriş Denemesi Yapıldı!")
        break
    elif parola == sys_pass and sys_kullanici_adi != kullanici_adi:
        print("Kullanıcı Adı Hatalı!")
        deneme_hakki -= 1
    elif parola != sys_pass and sys_kullanici_adi == kullanici_adi:
        print("Hatalı Şifre!"),
        deneme_hakki -= 1
    elif parola != sys_pass and sys_kullanici_adi != kullanici_adi:
        print("Kullanıcı Adı ve Şifre Hatalı!")
        deneme_hakki -= 1
