data_list = [('яблоко', 10, 'груша'),
             ('кот', 5, 'собака'),
             ('стул', 15, 'стол'),
             ('жара', 20, 'холод')]


sorted_1 = sorted(data_list, key=lambda x: x[2])
sorted_2 = sorted(data_list, key=lambda x: x[1], reverse=True)
sorted_3 = sorted(data_list, key=lambda x: len(x[0]))

print("Сортировка по третьему элементу:")
print(*sorted_1, sep="\n")
print()

print("Сортировка по второму элементу:")
print(*sorted_2, sep="\n")
print()

print("Сортировка по длине первого элемента:")
print(*sorted_3, sep="\n")
