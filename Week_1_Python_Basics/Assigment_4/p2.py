# Shopping Bill Generator

product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

# Calculations
total_cost = quantity * price
gst = total_cost * 0.18
final_bill = total_cost + gst

# Bill Display
print("\n----- SHOPPING BILL -----")
print("Product Name :", product_name)
print("Quantity     :", quantity)
print("Price        :", price)
print("Total Cost   :", total_cost)
print("GST (18%)    :", gst)
print("Final Bill   :", final_bill)