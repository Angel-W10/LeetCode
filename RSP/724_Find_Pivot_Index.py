def pivotIndex(nums: list[int]) -> int:
    # lsum, rsum = 0, 0
    # for i in range(len(nums)):
    #     lsum = sum(nums[:i])
    #     rsum = sum(nums[i+1:])
    #     if(lsum==rsum):
    #         return i

    # total = sum(nums)
    # pivot = -1
    # for i in range(len(nums)):
    #     psum = total - nums[i]
    #     lsum = sum(nums[:i])
    #     if lsum == psum/2:
    #         pivot = i
    # return pivot

    pivot = 0
    lsum = 0
    count = 0
    rsum = sum(nums) - nums[pivot]
    while(lsum!=rsum and count <  len(nums) and pivot < len(nums)-1):

        lsum+= nums[pivot]
        pivot+=1
        rsum-=nums[pivot]
        count+=1
    if(lsum==rsum):
        return pivot
    else:
        return -1




if __name__ == "__main__":
    nums = [-1,-1,0,1,1,0]
    print(pivotIndex(nums))