    # sum_lens=[]
    # temps = []
    # for i in range(len(nums)):
    #     count=0
    #     temp = []
    #     for j in range(i, len(nums)):
    #         if(abs(nums[i] - nums[j]) in {0, 1}):
    #             count+=1
    #             temp.append(nums[j])
    #     sum_lens.append(count)
    #     temps.append(temp)
    # print(temps)
    # print(sum_lens)
    # if(max(temps)==nums):
    #     return 0
    # print(max(sum_lens))
    # if (max(sum_lens)<2):
    #     return 0
    # return max(sum_lens)



########################################
# USING A HASH MAP
# add in a hash map the values and their count

# then go through the hash map and check if we have a (i+1) value present, 
# yes then add both counts = out
# got for the next one
# out = max(out)
from collections import defaultdict


def findLHS(nums: list[int]) -> int:
    mydict = defaultdict(int)
    res = 0
    for i in nums:
        if(i in mydict):
            mydict[i]+=1
        else:
            mydict[i]=1

        if (i+1) in mydict:
            res = max(res, mydict[i] + mydict[i+1])
        if (i-1) in mydict:
            res = max(res, mydict[i]+mydict[i-1])
    return res









if __name__ == "__main__":
    # nums =[1,3,2,2,5,2,3,7]
    nums = [1, 1, 1, 1]
    print(findLHS(nums))


