# Pattern A

# num = int(input("Enter a number: "))
# for i in range(num):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Pattern B

# num = int(input("Enter a number: "))
# for i in range(num):
#     for j in range(1, num - i + 1):
#         print("*", end=" ")
#     print()


# Pattern C

num = int(input("Enter a number: "))
for i in range(1 , num + 1):
    #print spaces

    for j in range(num - i):
        print(" ", end="")

    #print stars
    for j in range(i):
        print("* ", end=" ")
    print()