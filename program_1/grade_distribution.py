marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = float(input(f"Enter average mark for student {i + 1}: "))
    marks.append(mark)

grades = {
    "A+": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

for mark in marks:
    if mark >= 90:
        grades["A+"] += 1
    elif mark >= 80:
        grades["A"] += 1
    elif mark >= 70:
        grades["B"] += 1
    elif mark >= 60:
        grades["C"] += 1
    elif mark >= 50:
        grades["D"] += 1
    else:
        grades["F"] += 1

print("\n--- Grade Distribution ---")

for grade, count in grades.items():
    print(f"Grade {grade}: {count} student(s)")
