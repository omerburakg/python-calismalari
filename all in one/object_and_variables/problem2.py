# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.


boy = float(input("Boyunuzu metre türünden giriniz:"))
kilo = float(input("Kilonuzu kg cinsinden giriniz:"))

bmi = kilo / (boy * boy)
print("BMI oranınız: {}".format(bmi))
