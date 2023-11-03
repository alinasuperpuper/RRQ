def main():
    print('Цена первого товара:')
    a = int(input())
    
    print('Цена второго товара:')
    b = int(input())
    
    print('Цена третьего товара:')
    c = int(input())
    
    if a > b > c:
        print('Акция!')
        print(f'К оплате: {(a + b + c) // 3}')
    
    elif a < b < c:
        print('Акция!')
        print(f'К оплате: {(a + b + c) // 2}')
    
    else:
        print(f'К оплате: {a + b + c}')
if __name__ == "__main__":
    main()    
