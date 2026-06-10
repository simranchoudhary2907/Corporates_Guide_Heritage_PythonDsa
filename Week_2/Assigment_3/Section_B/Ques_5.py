# a) Create and unpack tuple
employee = ('Rajesh Kumar', 34, 'Data Analyst', 75000, 'Bangalore')

name, age, designation, salary, city = employee

print("Name:", name)
print("Age:", age)
print("Designation:", designation)
print("Salary:", salary)
print("City:", city)

# b) Use * operator for unpacking
first, *middle, second_last, last = employee

print("First Item:", first)
print("Middle Items:", middle)
print("Last Two Items:", second_last, last)

# c) Swap values in a single line
x, y, z = 10, 20, 30

x, y, z = z, x, y

print("x =", x)
print("y =", y)
print("z =", z)

# d) Tuple unpacking in a loop
data = [('Alice',90), ('Bob',85), ('Charlie',78), ('Diana',92)]

for name, score in data:
    print(f"{name} scored {score}/100")

# e) Function returning min and max as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [12, 45, 7, 89, 34]

minimum, maximum = min_max(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)