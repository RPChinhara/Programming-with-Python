def duplicate(nums: list):
    return list(set([x for x in nums if nums.count(x) > 1]))

arr = [1, 2, 2, 3, 4, 5, 5, 6]
print(duplicate(arr))