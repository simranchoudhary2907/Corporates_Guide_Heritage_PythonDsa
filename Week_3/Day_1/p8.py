cart = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500
}

# Add new product
cart["Headphones"] = 2000

# Update existing product price
cart["Mouse"] = 600

# Remove product
cart.pop("Keyboard")

# Total cart value
total = sum(cart.values())

print("Shopping Cart:", cart)
print("Total Cart Value:", total)