from ast import List
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) in [0, 1]:
            return 0
        MAX = 99999
        '''
        greedy approach

        select one point:
        check the next point and keep the distance
        go throught each point 
        and keep the point with the min distance that is not already
        connected to the goven point

        add the points in a new array to keep track of them

        return the final total distance

        p = 5,2
        d = 4
        7, 0 -> 4




        dict: {
            00:22,
            22:52,
            310: 22,
            52: 70
        }

        total d = 4 + 3 + 9 + 4 = 20

        Idea: MST 

        Until number of nodes used != n

        have an array to see if the node is in the MST
        go through each node and update the distances, get the min distance
        add that node to the mst
        Update the distances of the nodes not in MST


        '''

        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    

        n = len(points)
        num_used = 0
        distances = [math.inf]*n
        distances[0] = 0
        in_use = [False]*n
        ans = 0

        while num_used < n:
            cur_node = -1
            cur_dist = math.inf

            # go through each node and update the distances, get the min distance
            for node in range(n):
                if not in_use[node] and distances[node] < cur_dist:
                    cur_dist = distances[node]
                    cur_node = node
            
            in_use[cur_node] = True
            num_used+=1
            ans+=cur_dist

            # Update the distances of the nodes not in MST

            for next_node in range(n):
                if not in_use[next_node]:
                    w = get_dist(points[next_node], points[cur_node])
                    if w < distances[next_node]:
                        distances[next_node] = w
            # print

        return ans

                







                    



        # connections = collections.defaultdict(list)
        # c = 0
        # # connections = {}
        # ans = 0
        # d_list = []

        # for i in reversed(points):

        #     point1 = [0, 0]
        #     point2 = [0, 0]

        #     dist = MAX

        #     for j in points:
        #         print(i, j)
        #         if ((j!=i) and (connections[tuple(j)] != tuple(i) and connections[tuple(i)] != tuple(j))):
        #             # connect is not there already
        #             temp = get_dist(i, j)
        #             print(str(i) + " " + str(j) + " temp = " + str(temp))
        #             if (temp < dist):
        #                 dist = temp
        #                 point1 = i
        #                 point2 = j

        #     # adding the point to the dict                        
        #     connections[tuple(point1)] = tuple(point2)
        #     d_list.append(dist)
        #     print("dist = " + str(dist))
                    
        #     ans+=dist
        #     print("ANSWER: " + str(ans))
        #     print(connections.items())
        #     print("\n")
        #     c+=1
           

        #     # if c == n-1:
        #     #     return ans
        # print(d_list)
        # d_list[d_list.index(max(d_list))] = 0
        # ans = sum(d_list)

        # return ans


        # # c = 0
        # # n = len(points)
        # # mst = [points[c]]
        # # ans = 0

        # # while (len(mst)<n):
        # #     print("mst = " + str(mst))
        # #     for i in mst:
        # #         dist = MAX
        # #         point = [0, 0]
        # #         for j in points:
        # #             if j not in mst:
        # #                 temp = get_dist(i, j)
        # #                 print(i, j, temp)
        # #                 if (temp < dist):
        # #                     dist = temp
        # #                     point = j
        # #         mst.append(point)
        # #         ans+=dist
        # #         print("ANS: " + str(ans))

        # # return ans