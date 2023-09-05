# Fibonacci Serisi
print(
    """
*******************************************
            FIBONACCI HESAPLAMA
*******************************************
"""
)

a = 1
b = 1
liste = []
for i in range(50):
    a, b = b, a + b
    liste.append(b)
print(liste)
