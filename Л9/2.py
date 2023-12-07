def main():
        l1 = input().split(';')  # Разделяем строку на список строк, используя ";" в качестве разделителя
    l2 = []  # Разделяем каждую строку в списке на подсписки по символу ","
    for i in l1:
        l2.append(i.split(','))
    
    for row in l2:  # Для каждого подсписка в l2
        for el in row:  # Для каждого элемента в подсписке
            if int(el) >= 1000000000:  # Если элемент больше или равен 1000000000
                print(el, end=' ')  # Выводим его
    
        print()  # Переход на новую строку после обработки подсписка
if __name__ == "__main__":
    main()
