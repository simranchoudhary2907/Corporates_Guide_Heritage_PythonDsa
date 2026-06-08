age = int(input("Enter age: "))
group_size = int(input("Enter group size: "))

if age >= 18:
    if age >= 60:
        ticket_price = 100
    else:
        ticket_price = 200
else:
    if age < 5:
        ticket_price = 0
    else:
        ticket_price = 80

total = ticket_price * group_size

if group_size > 10:
    total = total * 0.8

print("Total Bill =", total)