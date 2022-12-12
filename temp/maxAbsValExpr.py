# BRUTE FORCE APPROACH

# def helper(i, j, arr1, arr2):
#     return abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)

# def maxAbsValExpr(arr1: list[int], arr2: list[int]) -> int:
    
#     i = 0
#     j = i+1
#     sum = -999999999
#     for i in range(len(arr1)-1):
#        for j in range(1, len(arr1)):
#         res = helper(i, j, arr1, arr2)
#         print(res, i, j)
#         if(res>sum):
#             sum = res
#     return sum



# if __name__ == "__main__":
#     arr1 = [2,2,6,1,-7,-1,-7]
#     arr2 = [6,1,-2,-10,-7,-6,-10]
#     print(maxAbsValExpr(arr1, arr2))



#############################################################################################################################
#############################################################################################################################


def maxAbsValExpr(self, x, y):
    res, n = 0, len(x)
    for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
        smallest = p * x[0] + q * y[0] + 0
        for i in range(n):
            cur = p * x[i] + q * y[i] + i
            res = max(res, cur - smallest)
            smallest = min(smallest, cur)
    return res


if __name__ == "__main__":
    arr1 = [2,2,6,1,-7,-1,-7]
    arr2 = [6,1,-2,-10,-7,-6,-10]
    print(maxAbsValExpr(arr1, arr2))

