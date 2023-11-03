def main():
    print('Категория:')
    a = input()
    
    if a == 'продукты':
        print('Цена:')
        b = int(input())
    
        if b <= 100:
            print('Попробуйте нашу выпечку!')
        elif 100 < b <= 500:
            print('Как насчет орехов в шоколаде?')
    
        else:
            print('Попробуйте экзотические фрукты!')
    
    else:
        print('Загляните в товары для дома!')
if __name__ == "__main__":
    main()
