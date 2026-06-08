a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

    sides = sorted([a, b, c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Also a Right-Angled Triangle")

else:
    print("Not a Valid Triangle")