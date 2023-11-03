def main():
    print('Покупатели за позавчера:')
    a = int(input())
    
    print('Покупатели за вчера:')
    b = int(input())
    
    if a < b:
        print(f'Сегодня магазин посетит: {b + (b - a)} человек')
    
    elif a > b:
        print(f'Сегодня магазин посетит: {b - (a - b)} человек')
if __name__ == "__main__":
    main()
