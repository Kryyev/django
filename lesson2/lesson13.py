src = open('src_14.txt', 'rt')
last_var = open('last_var.txt', 'wt')

stu_cnt = 0

for line in src:
    stu_cnt += 1
    lst = line.split()
    avg = round(sum(int(dig) for dig in lst[2:])/len(lst[2:]), 1)
    line = f'{lst[1] + " " + lst[0][0] + ".":<15}{avg}\n'
    if avg <5:
        print(line, end='')
    last_var.write(line)
print(f'Средняя по класу: {round(avg / stu_cnt * 10, 1)}')
src.close()
last_var.close()