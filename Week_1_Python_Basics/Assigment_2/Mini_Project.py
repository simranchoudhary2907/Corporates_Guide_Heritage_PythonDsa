name = input("Enter name: ")
emp_id = int(input("Enter ID: "))
salary = float(input("Enter salary: "))
department = input("Enter department: ")
active = input("Active (True/False): ")

active = bool(active)

print("\n--- Employee Profile ---")
print(f"Name: {name}")
print(f"ID: {emp_id}")
print(f"Salary: {salary:,.2f}")
print(f"Department: {department}")
print(f"Active: {active}")