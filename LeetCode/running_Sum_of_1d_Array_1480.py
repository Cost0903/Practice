from itertools import accumulate
import itertools 
import operator 

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): # for i in range(1,len(nums))
            if i > 0: nums[i] += nums[i-1] # nums[i] += nums[i=1]
        return nums

    def runningSum1(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
    
    def runningSum2(self, nums: List[int]) -> List[int]:
        db = []
        for i in range(len(nums)):
            if i == 0: db.append(nums[i])
            else: db.append((nums[i]+ db[i-1]))
        return db

    def runningSum3(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))  # accumulate 累加  

    def runningSum3(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums,operator.mul)) # 累乘 