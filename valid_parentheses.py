def is_valid(s: str) -> bool:
    stack = []
    matches = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            if len(stack) == 0:
                return False
            elif matches[stack.pop()] != c:
                return False


if __name__ == '__main__':
    tc = ["()", "()[]{}", "(]"]

    for t in tc:
        print(t, is_valid(t))
