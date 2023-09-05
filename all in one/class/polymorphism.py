class Employee:
    def raisee(self):
        raise_rate = 0.1
        return 100 + 100 * raise_rate


class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        return 100 + 100 * raise_rate


class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        return 100 + 100 * raise_rate


e1 = Employee()

c1 = CompEng()

e1 = EEE()


