from ast import List
import collections


def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        08:15 min
        brute force sol:
        go thourgh the list twice and check the sum for each pair of elements, 
        return the indcies if the sum == tagrget
        time: O(N^2)

        n = len(nums)

        for i in range(n):
            for j in range(n):
                if nums[i] + nums[j]==target and i!=j:
                    return [i, j]
        '''

        my_dict = collections.defaultdict(set)

        n = len(nums)

        for i in range(n):
            my_dict[nums[i]] = i

        for i in range(n):
            if (my_dict[target - nums[i]] and my_dict[target - nums[i]] != i):
                return [i, my_dict[target - nums[i]]]


