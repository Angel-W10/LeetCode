#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int> arr, int val){
    for (int i =0 ; i < arr.size(); i ++){
        if(arr[i]==val && arr[i]>0){
            cout<<arr[i]<<" "<<val<<endl;
            return true;
        }
    }
    return false;
}

bool checkIfExist(vector<int> arr) {
    if(arr.size()<1){
        return false;
    }
    for (int i = 0; i<arr.size(); i++){
        bool out = check(arr, 2*arr[i]);
        if(out == true){
            return true;
        }
    }
    return false;
}


int main(){


    // [-2,0,10,-19,4,6,-8]
    vector<int> arr;
    arr.push_back(-2);
    arr.push_back(0);
    arr.push_back(10);
    arr.push_back(-19);
    arr.push_back(4);
    arr.push_back(6);
    arr.push_back(-8);

    cout<<checkIfExist(arr);



    return 0;
}