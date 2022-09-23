print('Все ученики с их оценками')
print()
studensMain = ('Говорухи А. 5.83', 'Петров В. 4.92', 'Варфаломеев Г. 5.92',
               'Тюльпанов И. 4.08', 'Муромцев И. 5.42', 'Бессмертный К. 5.5',
               'Мухин М. 6.92', 'Мартынова М. 6.08', 'Николаев П. 5.17',
               'Гусева Г. 5.83', 'Тереньтьев С. 6.42', 'Трердолобов С. 5.33')
for students in studensMain:
    print(str(students))
#красивый вывод всех учеников с их оценками

from functools import reduce
avg = (5.83, 4.92, 5.92, 4.08, 5.42, 5.5, 6.92, 6.08, 5.17, 5.83, 6.42, 5.33)
lst_len = len(avg)
lst_avg = reduce(lambda x,y: x + y, avg)/ lst_len
print()
print('Средний балл по класу = ', lst_avg)
#Вывод среднего балла учеников с дальнейшим выводом

f = open('src.txt', 'r')
stu = f.read()
f.close()
stu = stu.split("\n")
pupils = []
for line in stu:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
    avarage = 0
    print('Ниже 5 баллов: ')
for p in pupils:
    avarage += int(p[2])
if p[2]<5:
    print(f"{p[0]} {p[1]}: {p[2]}")
    avarage /= len(pupils)
print(f'Средняя оценка по классу {avarage}')

#Тест второго способа вывода средней оценки + подсчет и вывод тех,у кого оценка ниже 5