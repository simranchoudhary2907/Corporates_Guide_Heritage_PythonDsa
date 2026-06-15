students = {
    "Rahul": 85,
    "Amit": 78,
    "Priya": 90,
    "Sneha": 82,
    "Karan": 77
}

print("Student Names:", list(students.keys()))
print("Marks:", list(students.values()))

average = sum(students.values()) / len(students)
print("Average Marks:", average)