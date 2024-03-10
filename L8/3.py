def nearby(data, places=1):
    return [x for x in data if '0' * places in x]

data = ['111', '101101', '11000']
print(*nearby(data), sep='\n')
