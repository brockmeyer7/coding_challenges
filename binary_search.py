def search(nums: list, target: int) -> int:
    idx = 0
    mid = len(nums) // 2
    if target > nums[-1] or target < nums[0]:
        return -1
    while len(nums) > 1:
        if target < nums[0]:
            return -1
        elif nums[0] <= target < nums[mid]:
            nums = nums[: mid]
            mid = len(nums) // 2
        else:
            idx += mid
            nums = nums[mid:]
            mid = len(nums) // 2
    if nums[0] == target:
        return idx
    return -1


if __name__ == '__main__':
    tc = [[[-1, 0, 3, 5, 9, 12], 9], [[-1, 0, 3, 5, 9, 12], 2], [[2, 5], 5]]

    for t in tc:
        print(t[0], t[1], search(t[0], t[1]))
