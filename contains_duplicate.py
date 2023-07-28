def contains_duplicate(nums: list) -> bool:
    nums_set = set()
    for n in nums:
        if n in nums_set:
            return True
        nums_set.add(n)
    return False


if __name__ == '__main__':

    lists = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

    for l in lists:
        result = contains_duplicate(l)
        print(l, result)
