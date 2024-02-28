def factorial(n):
    if n == 0:  # базовый случай: факториал 0 равен 1
        return 1
    else:
        return n * factorial(n-1)
