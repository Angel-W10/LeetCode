def isIsomorphic(s: str, t: str) -> bool:
    # using a hash map to map the strings and then seeing if they can change or not

    # create 2 hash maps for each chracter of s as value
    # the converted t character would be the key
    # and vice versa
    
    # if all of s can be stored without problem then true
    # else false

    # custom example: s =  "boolgg", t = "azzkpp"

    # strings s and t would always have 0 or 100 chars



    s_t = {}
    t_s = {}
    
    for c1, c2 in zip(s, t):
        if(c1 not in s_t and c2 not in t_s):
            s_t[c1] = c2
            t_s[c2] = c1

        elif (s_t.get(c1)!=c2 or t_s.get(c2)!=c1):
            return False
    
    return True



if __name__ == "__main__":
    s = "paper"
    t = "angel"
    print(isIsomorphic(s, t))
    # print(zip(s, t))
