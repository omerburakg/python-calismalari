def kareleri_al():
    for i in range(1,6):
        yield i **2

# generator bellekte daha az yer kaplaması için kullanılır.
generator = kareleri_al()

iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))