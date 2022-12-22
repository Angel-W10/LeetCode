def findMin(nums: list[int]) -> int:
    # low = 9999
    # i = 0
    # while i <= len(nums)/2:
    # # for i in range(len(nums)):
    #     j = len(nums)-i-1
    #     print(nums[i], nums[j])
    #     low = min(nums[i], nums[j], low)
    #     print(low)
    #     i+=1
    # return low
    l, r = 0, len(nums)-1
    while(nums[l]>nums[r]):
        m = (l+r)//2
        if(nums[m]>nums[r]):
            l = m+1
        else:
            r=m
    return nums[l]

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(findMin(nums))
