def main():
    kolvo = int(input())
    b = []
    for i in range(kolvo):
        names = input()
        b.append(names)
    for i in range(kolvo):
        print(b[i], i + 1)


if __name__ == "__main__":
    main()
