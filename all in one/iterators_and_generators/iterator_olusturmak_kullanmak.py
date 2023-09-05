liste = [1, 2, 3, 4, 5]
iterator = iter(liste)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
print(next(iterator))  # 5
# print(next(iterator))          #StopIteration error

print("-----------------------------------------------------")
iterator = iter(liste)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
# for döngüsünü aslında python bu şekilde yapıyor.

# kendi iterable objemizi oluşturalım.


class Kumanda:
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda = Kumanda(["ATV", "TRT", "KANAL D", "FOX", "BLOOMBERG"])
iterator = iter(kumanda)

for i in kumanda:
    print(i)
while True:
    a = input(":")
    if a == "x":
        print(next(iterator))
