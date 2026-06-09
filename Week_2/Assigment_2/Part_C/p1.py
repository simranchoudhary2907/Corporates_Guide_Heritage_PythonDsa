attempts = 0

while True:
    attempts += 1
    password = input("Enter Password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_length = len(password) >= 8

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    score = sum([has_length, has_upper, has_lower, has_digit, has_special])

    print("Length >= 8:", has_length)
    print("Uppercase:", has_upper)
    print("Lowercase:", has_lower)
    print("Digit:", has_digit)
    print("Special Character:", has_special)

    if score <= 2:
        print("Password Strength: Weak")
    elif score <= 4:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")
        break

print("Attempts =", attempts)