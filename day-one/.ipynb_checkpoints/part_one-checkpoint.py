import pandas as pd
file = pd.read_table('input.txt', delimiter=" ")
nums = file['num'].values


def measurement(nums):
    return [nums[i] > nums[i - 1] for i in range(len(nums))].count(True)

print(measurement(nums))