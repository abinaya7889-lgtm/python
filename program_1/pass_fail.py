marks = []

for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

pass_mark = 40

print("\n--- Pass/Fail Analysis ---")

for i, mark in enumerate(marks, start=1):
    if mark >= pass_mark:
        print(f"Subject {i}: {mark} - PASS")
    else:
        print(f"Subject {i}: {mark} - FAIL")

if all(mark >= pass_mark for mark in marks):
    print("Overall Result: PASS")
else:
    print("Overall Result: FAIL")
