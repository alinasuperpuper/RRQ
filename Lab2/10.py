def main():
    year = int(input())
    
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('да')
    else:
        print('нет')
if __name__ == "__main__":
    main()    
