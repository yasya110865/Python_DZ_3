

list_digits = []
digit_number = int(input('Введите количество элементов: '))
for i in range(1, digit_number+1):
    digit = int(input(f' Введите {i} элемент: '))
    list_digits.append(digit)
print(sorted(list_digits))