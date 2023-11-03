def main():
    n = False
    d = "+0123456789"
    phone = input()
    for d in phone:
        n = True
        break

    if phone:
        print("Правильно")
    else:
        print("Неправильный номер телефона")


if __name__ == "__main__":
    main()
