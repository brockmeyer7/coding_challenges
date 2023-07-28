def search(nums: list, target: int) -> int:
    start = 0
    end = len(nums) // 2
    while start != end:
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif nums[start] < target < nums[end]:
            nums = nums[: end + 1]
            end = len(nums) // 2
        else:
            nums = nums[end + 1]
