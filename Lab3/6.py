def main():
    n = 10000
    num = []
    for i in range(n + 1):
        num.append(i)
    num[1] = 0
    i = 2
    while i <= n:
        if num[i] != 0:
            j = 2 * i
            while j <= n:
                num[j] = 0
                j += i
        i += 1
    num = set(num)
    num.remove(0)
    print(sum(num))

if __name__ == "__main__":
    main()
