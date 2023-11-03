def main():
    bukva = input()
    a = ''
    kolvo = int(input())
    
    for i in range(kolvo):
        a += input()

    print(a.count(bukva))


if __name__ == '__main__':
    main()
