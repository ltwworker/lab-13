grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
 'Ursula': 4, 'Viktor': 5}

execl = []
good = []
satisf = []
bad = []

for student,grade in grades.items():
    print(f"{student}: {grade}")

    if grade == 5:
        execl.append(student)
    if grade == 4:
        good.append(student)
    if grade == 3:
        satisf.append(student)
    if grade <= 2:
        bad.append(student)
print('Студенты с отличными оценками:',execl)
print('Студенты с хорошими оценками:', good)
print('Студенты с удовлетворительными оценками:', satisf)
print('Студенты с плохими оценками:', bad)