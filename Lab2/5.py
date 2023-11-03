def main():
    n = int(input())
    m = int(input())
    if n % m == 0:
        print(n // m + 1)
    else:
        print(n // m)
if __name__ == "__main__":
    main()
