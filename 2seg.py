

list_digits = input('Введите элементы списка через запятую или любой другой ОДИН разделитель:')

int_list = []
for i in range(0, len(list_digits), 2):
    int_list.append(int(list_digits[i]))
print(set(int_list))
