# 1 задание
def groundhog_day(a):

    for i, (prev, curr) in enumerate(zip(a, a[1:]), 1):
        res = [i for i, (x, y) in enumerate(zip(prev, curr)) if x != y]

        if len(res) > 2:
            return (i,) + tuple(res)

    return (0, 0)

# 2 задание
def gears(sh, n, m):

    first = {}
    second = {}

    for i in sh:
        for j in i:

            if j > 0:
                if j % n == 0:
                    rn = j // n

                    if rn not in first:
                        if rn in second:
                            return j, second[rn]
                        first[rn] = j

                if j % m == 0:
                    rm = j // m

                    if rm not in second:

                        if rm in first:
                            return first[rm], j

                        second[rm] = j

    return None, None

# 3 задание
def brackets(sequence):

    chars = '({[<>]})'

    for i in sequence:
        if i not in chars:
            sequence = sequence.replace(i, '')

    while '()' in sequence or '[]' in sequence or '{}' in sequence:
        sequence = sequence.replace('()', '')
        sequence = sequence.replace('[]', '')
        sequence = sequence.replace('{}', '')
        sequence = sequence.replace('<>', '')

    return False if sequence != '' else True


print(brackets('12 / (9) + 2 ()'))