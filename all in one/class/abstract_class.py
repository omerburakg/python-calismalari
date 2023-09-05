from abc import ABC, abstractmethod

# abstract class'lar soyut classlar olarak da adlandırılır.
# inheritance için super class = parent class , sub class = child class


# abstract class, child classda methodları kullanmak zorunda olduğumuz ve super classtan obje oluşturamadığımız class çeşididir.


class Animal(ABC):  # super class
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Bird(Animal):  # sub class
    def __init__(self):
        print("bird")

    def walk(self):
        print("walk")

    def run(self):
        print("run")


b1 = Bird()
