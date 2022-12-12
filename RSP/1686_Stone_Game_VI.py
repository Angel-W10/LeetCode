# def stoneGameVI(aliceValues: list[int], bobValues: list[int]) -> int:
#     Asum, Bsum = 0, 0

#     def optimal_choice(a, b, p):
#         i = a.index(max(a))
#         j = b.index(max(b)) 

#         if(a[i]+ b[i] >= a[j] + b[j]):
#             # choice = i
#             print("choice: ", end = "")
#             print(i)
#             if(p==0):
#                 # alice's turn
#                 out = a[i]
#                 a[i], b[i] = -1, -1
#             else:
#                 out = b[i]
#                 a[i], b[i] = -1, -1

#         else:
#             # choice = j
#             print("choice: ", end = "")
#             print(j)
#             if(p==0):
#                 out = a[j]
#                 a[j], b[j] = -1, -1

#             else:
#                 out = b[j]
#                 a[i], b[i] = -1, -1
        
#         return out, a, b
#     print(Asum, Bsum, aliceValues, bobValues)
#     while (sum(aliceValues) != -1*len(aliceValues)):
        
#         choice, aliceValues, bobValues = optimal_choice(aliceValues, bobValues, 0)
#         Asum += choice
#         print(Asum, Bsum, aliceValues, bobValues)
#         if (sum(aliceValues) == -1*len(aliceValues)):
#             break
#         choice, aliceValues, bobValues = optimal_choice(aliceValues, bobValues, 1)
#         Bsum += choice
#         print(Asum, Bsum, aliceValues, bobValues)
    
    
#     if(Asum>Bsum):
#         return 1
#     elif(Bsum>Asum):
#         return -1
#     else:
#         return 0
                


# if __name__ == "__main__":
#     A = [9,9,5,5,2,8,2,4,10,2,3,3,4]
#     B = [9,5,3,4,4,6,6,6,4,3,7,5,10]

#     print(stoneGameVI(A, B))

        
def stoneGameVI(aliceValues: list[int], bobValues: list[int]) -> int:
    ScoreCard = []
    n = len(aliceValues)
    for i in range(n):
        ScoreCard.append([aliceValues[i]+ bobValues[i], aliceValues[i], bobValues[i]])

    ScoreCard.sort(reverse=True)
    a, b = 0, 0
    for i in range(n):
        if(i%2==0):
            a+=ScoreCard[i][1]
        else:
            b+=ScoreCard[i][2]

    if(a==b):
        return 0
    elif(a>b):
        return 1
    else:
        return -1







if __name__ == "__main__":
    A = [9,9,5,5,2,8,2,4,10,2,3,3,4]
    B = [9,5,3,4,4,6,6,6,4,3,7,5,10]

    print(stoneGameVI(A, B))