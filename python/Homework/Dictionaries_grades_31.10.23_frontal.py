students_score = {"momy": 20,
                  "yoel": 50,
                  "mendy": 71,
                  "yossy": 82,
                  "mosghy": 93
                  }
studens_grades = {}
for grade in students_score:
    if students_score[grade] < 70:
        studens_grades[grade] = "You failed."
    elif 70 <= students_score[grade] < 80:
        studens_grades[grade] = "You can do more."
    elif 80 <= students_score[grade] < 90:
        studens_grades[grade] = "Beyond expectations."
    else:
        studens_grades[grade] = "Amazing."

print(studens_grades)