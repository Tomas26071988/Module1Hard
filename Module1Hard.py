grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]       # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}              # множество
#   print(grades)
#   print(students)
A = grades[0]    # выдернул первый массив
#   print(A)
First_grades = sum(A)/len(A)     # среднее арифметическое для первого
#   print(First_grades)
B = grades[1]
second_grade = sum(B)/len(B)      # средне арифметическое второго
#   print(second_grade)
C = grades[2]
third_grade = sum(C)/len(C)
#   print(third_grade)
D = grades[3]
fourth_grade = sum(D)/len(D)
#   print(fourth_grade)
E = grades[-1]
fifth_grade = sum(E)/len(E)
#   print(fifth_grade)
res = list(students)        # перевод "множество" в "список"
#   print(type(res))
res.sort()               # сортировка списка по алфавиту
#   print(res)
first_student = res[0]   # "изъял" из списка первый объект
second_student = res[1]
third_student = res[2]
fourth_student = res[3]
fifth_student = res[-1]
#   print(first_student, second_student, third_student, fourth_student, fifth_student)
result_ = {first_student: First_grades, second_student: second_grade, third_student: third_grade, fourth_student: fourth_grade, fifth_student: fifth_grade}
print(result_)
