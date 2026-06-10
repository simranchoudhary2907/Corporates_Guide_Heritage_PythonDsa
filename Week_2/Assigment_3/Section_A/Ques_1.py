# a) Create a list called student_marks with 10 integer values
student_marks = [78, 85, 92, 67, 74, 88, 95, 81, 69, 90]

# b) Print first 3 elements, last 3 elements, and every alternate element
print("First 3 elements:", student_marks[:3])
print("Last 3 elements:", student_marks[-3:])
print("Every alternate element:", student_marks[::2])

# c) Print total number of elements
print("Total number of elements:", len(student_marks))

# d) Update the 5th element to 95
student_marks[4] = 95
print("Updated list:", student_marks)

# e) Print the list in reverse order using slicing
print("Reversed list:", student_marks[::-1])

# Original list remains unchanged
print("Original list:", student_marks)