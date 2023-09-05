# Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
# Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

liste = [i for i in range(1, 101) if i % 2 == 0]
liste.insert(0, 0)
print(liste)
