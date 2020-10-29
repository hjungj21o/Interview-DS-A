def is_divisible(s, t):
    str = ""

    while len(str) < len(s):
        str += t
        if str == s:
            return True

    return False


def findSmallestDivisors(s, t):
    if is_divisible(s, t) is False:
        return -1

    str = ""
    for char in t:
        str += char
        if is_divisible(t, str):
            return len(str)
