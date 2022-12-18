# def checker(lists, l, k, p):
#     # goes thruugh the list and checks if its:
#     # - non empty
#     # - has less than k elements div by p
#     _k = 0
#     if l == [] or l in lists:
#         return False

#     for i in range(len(l)):
#         if l[i]%p==0:
#             _k+=1

#     # print(_k, k)
#     if(_k<=k):
#         return True
#     else:
#         return False








# def countDistinct(nums: list[int], k: int, p: int) -> int:
#    # make the sub arrays using for loops

#    # nested for loop to go through
#    # every element
#     lists = []
#     for i in range(len(nums)+1):
#         for j in range(i):
#             # print("Here")
#             # condition to check if nums[j:i] satisfies the condition
#             temp = nums[j:i]
#             print(temp)
#             print(checker(lists, temp, k, p))
#             if(checker(lists, temp, k, p)):
#                 lists.append(temp)
#     print(lists)
#     return len(lists)





# if __name__ == "__main__":
#     nums = [1,3,8,12]
#     k = 3
#     p = 3
#     print(countDistinct(nums, k ,p))

################################################################################


def countDistinct(nums: list[int], k: int, p: int) -> int:
    trie = {}
    s = len(nums)
    ans = 0
    for i in range(s):
        count = 0
        cur = trie
        for j in range(i, s):
            # go through each individual set and see if it exists
            num = nums[j]
            if(num%p==0):
                count+=1
            # if count>k, break
            if count > k:
                break
            # else add it to cur and cur = cur[num]
            if num not in cur:
                cur[num] = {}
                ans+=1
            cur = cur[num]

    return ans


if __name__ == "__main__":
    nums = [1,3,8,12]
    k = 3
    p = 3
    print(countDistinct(nums, k ,p))