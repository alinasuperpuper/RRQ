def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest
