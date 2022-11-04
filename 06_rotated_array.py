def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end)//2

        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

nums = [8, 11, 13, 15, 1, 4, 6]
target = 4

index = search(nums, target)

print("Element was found at index:", index)