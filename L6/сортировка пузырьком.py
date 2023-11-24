def main():
n = 6     # размер массива
mas = [5, 7, 4, 3, 8, 2]
count = 0
for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]

    print(mas)
print(count)
if __name__ == "__main__":
    main()
