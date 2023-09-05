# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın

print(
    """       ÇARPIM TABLOSU
******************************************
            ÇARPIM TABLOSU
******************************************
"""
)

for i in range(1, 11):
    print("***************************************")
    for j in range(1, 11):
        print("{} ile {} çarpımı = {}".format(i, j, i * j))
