def main():
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = int(input())
    if b + 3 > len(alph):   # если б + 3 больше
        a = alph * 2    # дублируем алфавит на два
        print(alph[b - 1:b + 3])   # выводим нужный срез
    else:
        print(alph[b - 1:b + 3])   # выводим нужный срез
if __name__ == "__main__":
    main()
