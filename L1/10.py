def main():
    s = set()    # создаем пустое множ
    s1 = set('gtgae')    # создаем заполненное множество
    s.update('vccvpo', 'kbvc')    # добавляем в множество несколько элементов
    s.add('l')    # добавляем в множество 1 эл
    s_union = s.union(s1)     # объединяем множества
    s_union.pop()    # убираем рандом. элемент из множетсва
    s_isctn = s.intersection(s1)    # пересечение множеств
    s_symmdif = s.symmetric_difference(s1)    # эл, встреч в одном множестве, но не встреч в обоих
if __name__ == "__main__":
    main()    
