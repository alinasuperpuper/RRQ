def main():
    t1 = input()
    t2 = input()
    if t1 != t2 and (t1 == 'Тула' and t2 != 'Пенза' or t2 == 'Пенза' and t1 != 'Тула'):
        print('ДА')
if __name__ == "__main__":
    main()
