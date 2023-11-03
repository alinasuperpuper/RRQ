def main():
    a = input()
    if ((int(a[0]) + int(a[2])) % 8 != 0) and a[1] == '3':
        print('Подходит')
    else:
        print(f'{int(a[0]) + int(a[2])} {a[1]}')
if __name__ == "__main__":
    main()
