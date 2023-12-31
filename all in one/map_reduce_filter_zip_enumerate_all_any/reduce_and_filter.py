from functools import reduce

# Problem 3
# Elinizde şöyle bir liste bulunsun.

#   [1,2,3,4,5,6,7,8,9,10]

# Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

# *Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift = list(filter(lambda x: x % 2 == 0, liste))

print(reduce(lambda x, y: x + y, cift))
