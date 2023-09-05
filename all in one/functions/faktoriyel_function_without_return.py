def faktoriyel(sayi):
    faktoriyel = 1
    if sayi == 1 or sayi == 0:
        print("Faktöriyel:", faktoriyel)
    elif sayi > 1:
        for i in range(1, sayi + 1):
            faktoriyel *= i
        print(faktoriyel)
    else:
        print("Negatif Değerlerin Faktöriyeli Tanımsızdır.")


faktoriyel(10)
