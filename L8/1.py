s = input('Введите предложение: ').split()
max_len = len(max(s, key=len))

result = list(map(lambda x: x.rjust(max_len, "*"), s))
print(*result, sep="\n")
