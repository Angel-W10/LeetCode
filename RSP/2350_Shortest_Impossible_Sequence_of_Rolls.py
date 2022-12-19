    # Input: rolls = [4,2,1,2,3,3,2,4,1], k = 4
    # all_solutions = []
    # Output: 3
    
    # BRUTE FORCE APPROACH:
    # USING K GET EACH SOLUTION
    # CHECK IF THE SOL IS AVAILABLE FROM ROLLS
    # IF NOT BREAK, RETURN CURRENT K/LEN OF SOLUTION
    # O(SUM I = 0 TO K: I!) ~ NOT GOOD 

    #   1 2 3 4 

    # have a function to calculate all the solutions for k
    # go through the all_solutions list and see if you can make it in the rolls
    # is not return len of all_sol element
    # O(n^3)

    # A sequence of rolls of length len is the result of rolling a k sided dice len times.

    # len = 2
    # k = 3
    # [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]


def shortestSequence(rolls, k):
    res = 1
    s = set()
    for a in rolls:
        s.add(a)
        if len(s) == k:
            res += 1
            s.clear()
        # print(res)
    return res







    
if __name__ == "__main__":
    print(shortestSequence([4,2,1,2,3,3,2,4,1], 1))