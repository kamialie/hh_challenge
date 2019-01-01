#найти наименьшее натуральное число в массиве, в котором до 1е6 чисел, массив дан как последовательность чисел через пробел
##если положительных чисел нет - 1, если наименьшее не найдено - следующее после последнего

#raw_input = open('case_A').read()
raw_input = input()
#raw_input = '8 6 9 81 -5'
#raw_input = '6 9 5 4 3 2 1'
for i in range(1,len( raw_input.split())+2):
    if str(i) in  raw_input.split():
        continue
    else:
        print(i)
        break
