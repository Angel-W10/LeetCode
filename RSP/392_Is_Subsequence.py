def isSubsequence(s: str, t: str) -> bool:
        k = 0
        c = 0
        if(len(s)==0):
            return True
        for i in t:
            if(i==s[c]):
                c+=1
                k+=1
            if(k==len(s)):
                return True

        return False