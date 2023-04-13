

# list_1 = input('Введите элементы списка через запятую: ')
# list_1 = [int(list_1[i]) for i in range(0, len(list_1), 2)]
# list_2 = input('Введите элементы списка через запятую: ')
# list_2 = [int(list_2[i]) for i in range(0, len(list_2), 2)]
# for i in list_1:
#     if i in list_2:
#         list_1.remove(i)
# print(list_1)

# если не цифры
list_1 = input('Введите элементы списка через запятую: ')
list_1 = list_1.split(',')
list_2 = input('Введите элементы списка через запятую: ')
list_2 = list_2.split(',')
for i in list_1[:]:
    if i in list_2:
        list_1.remove(i)
print(list_1)



