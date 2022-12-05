
# def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
#     while(k!=0):
#         nums[ nums.index(min(nums))] = -nums[ nums.index(min(nums))]
#         k-=1
#         print(nums, k)

#     return sum(nums)
import heapq

def largestSumAfterKNegations(self, A, K):
    heapq.heapify(A)
    while K:
        heapq.heapreplace(A, -A[0])
        K -= 1
    return sum(A)


if __name__ == "__main__":
    A = [4, 2, 3]
    k = 1
    print(largestSumAfterKNegations(A, k))