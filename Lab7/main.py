import sys
#rows_num = int(input("Введіть розмір квадратної матриці: "))
with open('C:\\Users\\Oleksandr Mytsenko\\Documents\\CPPT\\CPPTLabs\\CPPT_Mytsenko_OS_KI-306_1\\Lab8\\binary_file.bin', 'rb') as file:
    data = file.read(4)
    rows_num = int.from_bytes(data, byteorder='big')
lst = []
filler = input("Введіть символ-заповнювач: ")
middle = rows_num//2
# цикл який виводить завдання під варіантом №10
for i in range(rows_num):
    lst.append([])

    # цикл який виводить пропуски
    if(i>=middle):
     for k in range(rows_num - i):
      print(' ', end='\t')
    else:
        for l in range(middle - i):
         print(' ', end='\t')

    # цикл який виводить масив
    for j in range(i+1):
        if len(filler) == 1:
            lst[i].append(ord(filler))
            print(chr(lst[i][j]), end="\t")
        elif len(filler) == 0:
            print("Не введено символ-заповнювач")
            sys.exit(1)
        else:
            print("Забагато символів-заповнювачів")
            sys.exit(1)
    # вивід нового рядка
    print()