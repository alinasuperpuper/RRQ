def main():
        l1 = []
    for i in range(int(input())):
        l1.append(int(input()))
        
    l2 = []
    
    for i in range(len(l1)):
        for j in range(i, len(l1)):
            l2.append(abs(l1[i] - l1[j]))
    
    l2 = list(set(l2))  # Убираем повторяющиеся элементы
    l2.sort()  # Сортируем в порядке возрастания
    print(l2)
if __name__ == "__main__":
    main()
