class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        '''
        make 2 arrays
        arrays have word count for each letter in both the words
        ,then check the differences of the counts, 
        if a diff is > 3 return False
        else
        check all, 
        then return true






        '''
        

        c1, c2 = [0]*26, [0]*26

        for i in word1:
            c1[ord(i)-ord('a')] +=1

        for i in word2:
            c2[ord(i)-ord('a')] +=1

        print(c1)
        print(c2)

        for i in range(26):
            if(abs(c1[i]-c2[i]) > 3):
                return False



        return True




