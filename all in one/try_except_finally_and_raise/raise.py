def terscevir(s):
    if type(s) != str:
        raise ValueError("Lütfen string bir değer gönderin.")
    else:
        return s[::-1]


print(terscevir(" Naber "))
print(terscevir(12))
