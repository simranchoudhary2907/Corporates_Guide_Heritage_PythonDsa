# a) Create a dictionary called 'student'

student = {
    "name": "Simran Kumari",
    "age": 20,
    "course": "B.Tech CSE",
    "city": "Darbhanga",
    "gpa": 8.5
}

# b) Access and print each value using [] notation

print("Using [] notation:")
print(student["name"])
print(student["age"])
print(student["course"])
print(student["city"])
print(student["gpa"])

# Access and print each value using .get() method

print("\nUsing get() method:")
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print(student.get("city"))
print(student.get("gpa"))

# c) Add two new keys: email and phone

student["email"] = "simran@example.com"
student["phone"] = "9876543210"

print("\nUpdated Dictionary:")
print(student)

# d) Update GPA and delete city

student["gpa"] = 8.8
del student["city"]

print("\nAfter Updating GPA and Deleting City:")
print(student)

# e) Check if keys exist

print("\nChecking Keys:")
print("name" in student)      # True
print("address" in student)   # False

# f) Print total number of key-value pairs

print("\nTotal key-value pairs:", len(student))