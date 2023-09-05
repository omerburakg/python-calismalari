def calc(x):
    # your code goes here
    return (side * 4, side**2)


side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))
