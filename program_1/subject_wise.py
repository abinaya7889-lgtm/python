students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    student_marks = []

    print(f"\nStudent {i + 1}")
    for j in range(subjects):
        mark = float(input(f"Enter mark for Subject {j + 1}: "))
        student_marks.append(mark)

    marks.append(student_marks)

print("\n--- Subject Analysis ---")

for j in range(subjects):
    subject_marks = [marks[i][j] for i in range(students)]

    average = sum(subject_marks) / students
    highest = max(subject_marks)
    lowest = min(subject_marks)

    print(f"\nSubject {j + 1}")
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
