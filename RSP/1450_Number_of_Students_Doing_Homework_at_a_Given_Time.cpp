#include <iostream>
#include <vector>

int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        /* 
        go thorugh the two lists
        if start time [i] < query timr and end time[i] > query time
        count++
        
        O(n) - time
        O(1) - space
        */

        int n = startTime.size();
        int count = 0;
        for (int i = 0; i < n ; i++){
            if (startTime[i] <= queryTime && endTime[i] >= queryTime){
                count++;
            }
        }
        return count;

        
    }