def is_valid(s: str):
    c1 = 0
    c2 = len(s) - 1
    while c2 > c1:
        if not s[c1].isalnum():
            c1 += 1
        elif not s[c2].isalnum():
            c2 -= 1
        else:
            if s[c1].lower() != s[c2].lower():
                return False
            c1 += 1
            c2 -= 1
    return True


if __name__ == '__main__':
    tc = ["A man, a plan, a canal: Panama", "race a car", "race car", "0P"]

    for t in tc:
        print(t, is_valid(t))
