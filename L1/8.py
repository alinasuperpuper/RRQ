def main():
    spisok = ['a', 'b', 'c', 'd', 'e']   # создаем заполненный список
    
    spisok.append('f')   # добавляем элемент
    spisok.remove('a')   # убираем элемент
    spisok2 = spisok[2:5]   # срез списка
    spisok3 = spisok[::-1]   # список наоборот
    spisok.reverse()   # список наоборот
    
    
    s4 = [['aasd', 'qew', 'gfg'], ['a', 'b', 'c']]   # двумерный список
    print(s4[1][2])   # выводим второго элемент первого списка
    
    spisok.clear()   # очищаем список
if __name__ == "__main__":
    main()
