# Challenge 1 — Student Report System

students = [
    {'name': 'Amit', 'roll': 1, 'subjects': {'Math': 88, 'Science': 76, 'English': 81}},
    {'name': 'Priya', 'roll': 2, 'subjects': {'Math': 92, 'Science': 89, 'English': 90}},
    {'name': 'Rahul', 'roll': 3, 'subjects': {'Math': 45, 'Science': 55, 'English': 60}},
    {'name': 'Sneha', 'roll': 4, 'subjects': {'Math': 78, 'Science': 82, 'English': 75}},
    {'name': 'Rohan', 'roll': 5, 'subjects': {'Math': 35, 'Science': 60, 'English': 50}},
    {'name': 'Anjali', 'roll': 6, 'subjects': {'Math': 85, 'Science': 91, 'English': 88}},
    {'name': 'Karan', 'roll': 7, 'subjects': {'Math': 65, 'Science': 72, 'English': 70}},
    {'name': 'Neha', 'roll': 8, 'subjects': {'Math': 95, 'Science': 98, 'English': 96}},
    {'name': 'Vikas', 'roll': 9, 'subjects': {'Math': 50, 'Science': 45, 'English': 55}},
    {'name': 'Pooja', 'roll': 10, 'subjects': {'Math': 80, 'Science': 85, 'English': 83}}
]

# b) Function to calculate average marks
def get_average(student):
    return sum(student['subjects'].values()) / len(student['subjects'])

# c) Students who passed all subjects
passed_students = [
    student['name']
    for student in students
    if all(mark >= 40 for mark in student['subjects'].values())
]

# d) Subjects where at least one student scored below 50
low_score_subjects = set()

for student in students:
    for subject, marks in student['subjects'].items():
        if marks < 50:
            low_score_subjects.add(subject)

# e) Dictionary of subject-wise scores
subject_scores = {}

for student in students:
    for subject, marks in student['subjects'].items():
        if subject not in subject_scores:
            subject_scores[subject] = []
        subject_scores[subject].append(marks)

# Class average per subject
class_avg = {}

for subject, scores in subject_scores.items():
    class_avg[subject] = round(sum(scores) / len(scores), 2)

# f) Topper and rankings
topper = max(students, key=get_average)

ranked_students = sorted(
    students,
    key=get_average,
    reverse=True
)

# g) Subjects taken by all students
common_subjects = set(students[0]['subjects'].keys())

for student in students[1:]:
    common_subjects &= set(student['subjects'].keys())

# ---------------- OUTPUT ----------------

print("Students Passed All Subjects:")
print(passed_students)

print("\nSubjects with at least one score below 50:")
print(low_score_subjects)

print("\nSubject-wise Scores:")
print(subject_scores)

print("\nClass Average Per Subject:")
for subject, avg in class_avg.items():
    print(subject, ":", avg)

print("\nTopper:")
print(topper['name'], "-", round(get_average(topper), 2))

print("\nStudent Rankings:")
for rank, student in enumerate(ranked_students, start=1):
    print(rank, student['name'], "-", round(get_average(student), 2))

print("\nSubjects Taken By All Students:")
print(common_subjects)