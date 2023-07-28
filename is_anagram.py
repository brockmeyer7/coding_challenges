def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1

        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1

    if s_dict == t_dict:
        return True
    return False


if __name__ == '__main__':
    test_cases = [["anagram", "nagaram"], ["rat", "car"]]

    for t in test_cases:
        print(t[0], t[1], is_anagram(t[0], t[1]))
