class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        BRUTE FORCE SOLUTION

        ans = []
        for loop through height as i first
        visibility = 0
        for loop throgh (i+1, len(heoghts))
            if(min(h[i], h[j]) > max(heights[i+1:j])):
                visibility+=1
            
        array.append(visibility)


        10, 6, 8, 5, 11, 9

        0, -4, -2, -5, 1, -1



        '''

        # ans = []
        # if len(heights)==1:
        #     return ans
        
        # if len(heights)==2:
        #     return [1, 0]

        # for i in range(len(heights)):
        #     visibility = 0
        #     vis = 0
        #     for j in range(i+1, len(heights)):
        #         if abs(j-i)==1:
        #             visibility +=1
        #             vis = heights[j]
        #         elif (heights[j] >= vis and min(heights[i], heights[j]) > vis):
        #             visibility+=1
        #             vis = heights[j]
        #         else:
        #             continue
        #     # heights.pop(0)
        #         # print(heights[i], heights[j])
        #         # if abs(j-i)==1:
        #         #     visibility +=1
        #         # elif min(heights[i], heights[j]) > max(heights[i+1:j]):
        #         #     visibility +=1
        #         # else:
        #         #     continue
                
        #     ans.append(visibility)
        # return ans


    # SOLUTION USING MONOTONIC STACK

        n = len(heights)
        stk = []
 
        res = [0]*n
        for i in range(n-1, -1, -1):
            vis = 0
            cur = heights[i]
            while(stk and cur > stk[-1]):
                vis+=1
                stk.pop()

            if (stk):
                vis+=1

            stk.append(cur)
            res[i] = vis

        return res






