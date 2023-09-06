# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0

for height in student_heights:
    total_height += height

num_students = 0
for student in student_heights:
    num_students += 1

average_height = round(total_height / num_students)
print(average_height)


# Easier solution using Sum & Len
# total_height = sum(student_heights)
# num_students = len(student_heights)
# average_height = round(total_height / num_students)
# print(average_height)
