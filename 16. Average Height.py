student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_student = 0
total_height = 0
for student in student_heights:
    total_student += 1
    total_height += student

average_student_height = round(total_height / total_student)
print(average_student_height)