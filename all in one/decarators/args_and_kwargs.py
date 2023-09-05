# *args


def fonksiyon(*args):  # yıldız sayesinde esnek sayıda argüman gönderebiliyoruz.
    for i in args:
        print(i)


fonksiyon(1, 2, 3, 4, 5, 6, 7, 8, 9)


def fonksiyon(isim, *args):
    print("isim:", isim)

    print("-------------")
    for i in args:
        print(i)


fonksiyon(
    "Murat", 1, 2, 3, 4, 5, 6, 7
)  # Murat isim ile eşleşti, diğerleri args'a tuple olarak gitti.


# **kwargs


def fonksiyon(**kwargs):
    print(kwargs)


# fonksiyon(isim= "Burak",soyisim = "Goral",numara = "12345")
# **kwargs (keyward args) argümanlardan bir sözlük oluşturur.
# {'isim': 'Burak', 'soyisim': 'Goral', 'numara': '12345'}


def fonksiyon(**kwargs):
    for i, j in kwargs.items():
        print("Argüman ismi:", i, "Argüman değeri:", j)


fonksiyon(isim="Burak", soyisim="Goral", numara="12345")


def fonksiyon(*args, **kwargs):
    for i in args:
        print(i)

    print("------------------")
    for i, j in kwargs.items():
        print(i, j)


fonksiyon(
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, isim="Burak", soyisim="Goral", numara="12345"
)
# 1,2,3,4,5,6,7,8,9,0,10 args yerine geçecek, diğer eşleşenler ise kwargs olacaktır.
