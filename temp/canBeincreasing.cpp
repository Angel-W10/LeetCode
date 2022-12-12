#include <iostream>
#include <vector>
using namespace std;


bool canBeIncreasing(vector<int> nums) {

    for (auto i: nums){
        cout<<i<<endl;
    }
    return true;
}


int main(){

    vector<int> nums;

    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);


    canBeIncreasing(nums);

    return 0;
}