def two_sum(nums, target):
    n_dict = {}
    for i, n in enumerate(nums):
        goal = target - n
        if goal == n:
            if goal in n_dict:
                return [n_dict[goal], i]
        elif goal in n_dict:
            return [n_dict[goal], i]
        n_dict[n] = i


if __name__ == '__main__':
    tc = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]

    for t in tc:
        print(t[0], t[1], two_sum(t[0], t[1]))
