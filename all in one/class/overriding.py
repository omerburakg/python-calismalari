class Animal:  # parent class
    def toString(self):
        print("Animal")


class Monkey(Animal):
    def toString(self):
        print("Monkey")


a = Animal()
m = Monkey()


a.toString()
m.toString()  # monkey calls overriding method
