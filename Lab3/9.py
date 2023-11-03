def main():
    st = ''
    while True:
        word = input()

        if word != 'стоп':
            st += word

        else:
            break

    print(eval(st))


if __name__ == '__main__':
    main()
