# 2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i-1]]
print(result)
