# a) Create a tuple containing all 12 month names
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# b) Access and print required elements
print("3rd month:", months[2])
print("Last month:", months[-1])
print("Months from index 3 to 6:", months[3:7])

# c) Try to change the first element
try:
    months[0] = "January_New"
except TypeError as e:
    print("Error:", e)

# d) Create a single-element tuple containing your name
name = ("Simran",)
print("Single-element tuple:", name)
print("Type:", type(name))

# e) Convert tuple to list, add 13th month, convert back to tuple
months_list = list(months)
months_list.append("Intercalary")

months = tuple(months_list)

print("Updated tuple:", months)