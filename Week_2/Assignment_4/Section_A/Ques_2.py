# Inventory Dictionary
inventory = {
    'apple': 50,
    'banana': 30,
    'mango': 0,
    'cherry': 15,
    'grape': 0
}

# a) Print all product names
print("Products:")
print(inventory.keys())

# b) Print all quantities
print("\nQuantities:")
print(inventory.values())

# c) Print product and quantity using items()
print("\nInventory Details:")
for product, qty in inventory.items():
    print(f"{product}: {qty} units")

# d) Check quantity of papaya safely
print("\nPapaya Quantity:")
print(inventory.get("papaya", "Not available"))

# e) Remove mango and print popped value
removed = inventory.pop("mango")
print("\nRemoved Quantity:", removed)

# f) Add 3 new products using update()
inventory.update({
    "orange": 20,
    "pineapple": 10,
    "kiwi": 8
})

# g) Add watermelon only if it doesn't exist
inventory.setdefault("watermelon", 25)

# h) Print out-of-stock items
print("\nOut of Stock Products:")
for product, qty in inventory.items():
    if qty == 0:
        print(product)

print("\nUpdated Inventory:")
print(inventory)