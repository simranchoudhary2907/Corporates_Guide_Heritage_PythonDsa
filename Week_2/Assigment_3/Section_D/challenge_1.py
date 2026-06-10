# a) Create a list of 10 student records
students = [
    ("Alice", 101, [85, 90, 88, 92, 87]),
    ("Bob", 102, [70, 75, 68, 72, 74]),
    ("Charlie", 103, [95, 98, 96, 94, 97]),
    ("Diana", 104, [80, 82, 78, 85, 81]),
    ("Ethan", 105, [60, 65, 62, 58, 64]),
    ("Fiona", 106, [88, 86, 90, 89, 87]),
    ("George", 107, [73, 76, 71, 74, 75]),
    ("Hannah", 108, [91, 93, 89, 92, 94]),
    ("Ivan", 109, [67, 69, 70, 66, 68]),
    ("Julia", 110, [84, 86, 82, 85, 83])
]

# b) Function to calculate average
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

# c) Create (name, average_score) list using list comprehension
averages = [
    (name, calculate_average(marks))
    for name, roll, marks in students
]

print("Student Averages:")
for student in averages:
    print(student)

# d) Sort by average score (descending)
ranked_students = sorted(
    averages,
    key=lambda x: x[1],
    reverse=True
)

print("\nClass Rank:")
for rank, (name, avg) in enumerate(ranked_students, start=1):
    print(f"Rank {rank}: {name} - {avg:.2f}")

# e) Count students with average above 75
count = sum(1 for name, avg in ranked_students if avg > 75)

print("\nStudents scoring above 75 average:", count)

# f) Find topper and lowest scorer
topper = ranked_students[0]
lowest = ranked_students[-1]

print("\nTopper:")
print(f"{topper[0]} with average {topper[1]:.2f}")

print("\nLowest Scorer:")
print(f"{lowest[0]} with average {lowest[1]:.2f}")