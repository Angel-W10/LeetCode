def is_ascending(nums):
    #return true if is ascending else false
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            return False

    return True



def findSubsequences(nums):
        '''
        brute force go through each element combination
        and check if its ascending,
        yes: add to list
        no: move to the next one
        
        can use two pointers for this solution
        '''
    
        # make pointer l and r,
        l, r = 0, 0
        n = len(nums)
        subsets = []

        while (l < n):
            temp = nums[l:r] + nums[r:n]
            print(l, r, temp, nums[l:r], nums[r:n])
            # print(nums[0:0])
            if r > n:
                r = 0
                l+=1   
            if is_ascending(temp):
                if len(temp) > 1 and temp not in subsets:
                    subsets.append(temp)
            r+=1

        return subsets

if __name__ == "__main__":
    nums = [4,6,7,7]
    print(findSubsequences(nums))
