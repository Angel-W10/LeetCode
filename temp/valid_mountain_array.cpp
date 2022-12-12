// Given an array of integers arr, return true if and only if it is a valid mountain array.

// Recall that arr is a mountain array if and only if:

//     arr.length >= 3
//     There exists some i with 0 < i < arr.length - 1 such that:
//         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
//         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

#include <iostream>
#include <vector>

using namespace std;

int validMountainArray(vector<int>& arr) {
    int peak = arr[0];
    int len = arr.size();

    // go through the array 
    // and keep checking for the peak and its position
    for (int i = 0 ; i < len-1; i++){
        if(arr[i+1]==arr[i]){
            return -1;
        }
        if(arr[i+1]>arr[i]){
            peak = arr[i+1];
        }
        if(arr[i+1]<arr[i]){
            for (int j = i ; j < len - 1; j ++){
                if(arr[j+1]<!arr[j]){
                    return false;
                }
            }
            return true;
        }
        return true;

    }
    // when you find a peak keep checking if the remaining are stritctly decreasing


}


int main(){

    vector<int> arr;
    // arr.push_back(0);
    // arr.push_back(2);
    // // arr.push_back(3);
    // arr.push_back(3);
    // arr.push_back(5);
    // arr.push_back(2);
    // arr.push_back(1);
    // arr.push_back(0);
    arr.push_back(3);
    arr.push_back(5);
    arr.push_back(5);

    cout<<validMountainArray(arr)<<endl;

    return 0;
}