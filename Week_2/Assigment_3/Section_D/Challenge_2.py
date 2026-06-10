# a) Create a list of product tuples
inventory = [
    (101, "Laptop", 50000, 10),
    (102, "Mouse", 500, 3),
    (103, "Keyboard", 1200, 4),
    (104, "Monitor", 15000, 7),
    (105, "Printer", 8000, 2),
    (106, "Speaker", 2500, 6),
    (107, "Webcam", 1800, 1),
    (108, "Headphones", 3000, 8)
]

# b) Functions

def add_product(product):
    inventory.append(product)

def remove_product(name):
    global inventory
    inventory = [p for p in inventory if p[1] != name]

def update_quantity(name, qty):
    global inventory
    updated = []

    for pid, pname, price, quantity in inventory:
        if pname == name:
            updated.append((pid, pname, price, qty))
        else:
            updated.append((pid, pname, price, quantity))

    inventory = updated

# c) Total inventory value

def total_inventory_value():
    total = 0

    for pid, name, price, quantity in inventory:
        total += price * quantity

    return total

# Add product
add_product((109, "Tablet", 20000, 5))

# Remove product
remove_product("Speaker")

# Update quantity
update_quantity("Mouse", 12)

# Display inventory
print("Current Inventory:")
for product in inventory:
    print(product)

# Total inventory value
print("\nTotal Inventory Value:", total_inventory_value())

# d) Low stock alert
print("\nLow Stock Products (quantity < 5):")

for pid, name, price, quantity in inventory:
    if quantity < 5:
        print(name, "- Quantity:", quantity)

# e) Sort by price ascending
print("\nProducts Sorted by Price:")

sorted_products = sorted(inventory, key=lambda x: x[2])

for product in sorted_products:
    print(product)

# f) Search product by name
search_name = "Monitor"

print(f"\nSearching for '{search_name}':")

found = False

for product in inventory:
    if product[1].lower() == search_name.lower():
        print("Product Found:", product)
        found = True
        break

if not found:
    print("Product not found")