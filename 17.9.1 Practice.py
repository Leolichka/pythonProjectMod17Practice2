
""" запрашиваем у пользователя ввод данных"""
array_ = list(map(int,input('Введите последовательность чисел через пробел: ').split()))
chislo = int( input('Введите любое число: ',))
""" проверяем тип введенных данных"""
# print(type(array_))
# print(type(chislo))

""" Сортировка пузырьком """
for i in range(len(array_)):
    for j in range(len(array_) - i - 1):
        if array_[j] > array_[j + 1]:
            array_[j], array_[j + 1] = array_[j + 1], array_[j]
print(array_)

""" запускаем алгоритм на левой и правой границе"""
def binary_search(array_, chislo, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array_[middle] == chislo:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif chislo < array_[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array_, chislo, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array_, chislo, middle + 1, right)

"""анализ числа в списке"""
index = binary_search(array_, chislo, 0, len(array_) - 1)
if chislo not in array_:
     print(f'Нет числа {chislo} среди чисел последовательности. {array_}')
else:
    print("Ищем индекс введенного числа {}:".format(chislo))
    print("Индекс введенного числа {}: {}".format(chislo, binary_search(array_, chislo, 0, len(array_)-1)))
    if index == 0:
        print(f'Число {chislo} первое значение в списке, следующее - {array_[index + 1]}')
    elif index == int(len(array_) - 1):
        print(f'Число {chislo} последнее значение в списке, предыдущее значение - {array_[index - 1]}. Индекс позиции элемента, который меньше введенного пользователем числа: {index - 1}')
    else:
        print(f'Предыдущее значение - {array_[index - 1]}, следующее - {array_[index + 1]}. Индекс позиции элемента, который меньше введенного пользователем числа: {index - 1}')
