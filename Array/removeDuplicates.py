from typing import List

nums = [1, 1, 2, 2, 2, 4]
expectedNums = [1, 2, 4]

def removeDuplicates(nums: List[int]) -> int:
    if not nums: return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums [i-1]: nums[k] = nums[i]; k += 1
    return k

k = removeDuplicates(nums)

assert k == len(expectedNums)
print(k)

for i in range(k):
    assert nums[i] == expectedNums[i]

print("All tests passed!")