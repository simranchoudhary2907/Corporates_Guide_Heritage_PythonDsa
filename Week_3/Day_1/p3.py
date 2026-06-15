employees = {
    101: "Rahul",
    102: "Priya",
    103: "Amit",
    104: "Sneha"
}

emp_id = int(input("Enter Employee ID: "))

print(employees.get(emp_id, "Employee Not Found"))