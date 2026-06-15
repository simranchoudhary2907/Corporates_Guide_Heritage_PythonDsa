# Dictionary is used because student details
# are stored as key-value pairs.

students = {
    101: {"Name": "Rahul", "Course": "Python"},
    102: {"Name": "Priya", "Course": "Java"},
    103: {"Name": "Amit", "Course": "Data Science"}
}

# Set is used because course categories
# must be unique.

course_categories = {
    "Programming",
    "Data Science",
    "Web Development",
    "AI"
}

# List is used because multiple ratings
# can be stored and order may matter.

course_ratings = [4.5, 4.8, 4.2, 4.7, 5.0]

print("Student Details:")
print(students)

print("\nCourse Categories:")
print(course_categories)

print("\nCourse Ratings:")
print(course_ratings)