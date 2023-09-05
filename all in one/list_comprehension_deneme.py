liste1 = [[1, 2, 3, 4, 5, 6], [7, 8, "q", 9]]
liste2 = list()

for i in liste1:
    for x in i:
        liste2.append(x)
print(liste2)

liste3 = [[1, 2, 35, 134, 12], ["q", 231, "pek", 23]]
liste4 = [x for i in liste3 for x in i]
print(liste4)
