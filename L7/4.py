def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    elif s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
