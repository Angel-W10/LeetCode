def runningSum(self, nums: list[int]) -> list[int]:
        
        for i in range(len(nums)-1):
           nums[i+1] += nums[i]
        
        return nums



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    runningSum(nums)