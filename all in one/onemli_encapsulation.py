class BankAccount:
    def __init__(self, name, money, adress) -> None:
        self.name = name  # global
        self.__money = money  # private
        self.adress = adress

    # get and set global
    def getMoney(self):
        return self.__money

    def setMoney(self, amount):
        self.__money = amount

    # private : sadece class içinden müdahale edilebilir.
    def __increase(self):
        self.__money = self.__money + 500


# İki altçizgi koyduğumuz için erişim engellendi. Bu değeri ne görüntüleyebiliriz ne de dışarıdan değiştirebiliriz.
p1 = BankAccount("messi", 2000, "barcelona")

print(p1.getMoney())
p1.setMoney(5000)
print(p1.getMoney())
# p1.__increase() error AttributeError: 'BankAccount' object has no attribute '__increase'
# print(p1.getMoney())
