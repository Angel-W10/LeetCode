from ast import List


def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    '''

    go through the list
    check of the startTime is less and equal and endTime is greater and equal 
    that the query time

    if true 
    icrease counter

    '''

    n = len(startTime)
    count = 0
    for i in range(n):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            count+=1

    return count