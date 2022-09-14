#include <iostream>
#include <vector>

using namespace std;

vector <int> twoSum(vector<int>& nums, int target){

    vector <int> out;

    for (int i = 0 ; i < nums.size(); i++){
        for (int j = i; j < nums.size() ; j++){
            if (nums[i] + nums[j] == target){
                out.push_back(i);
                out.push_back(j);
            }
        }
    }

    return out;
}


int main(){

    vector <int> nums;
    nums.push_back(3);
    nums.push_back(7);
    nums.push_back(3);
    vector <int> out;
    out = twoSum(nums, 10);

    for (int i = 0;i<out.size();i++){
        cout<<out[i]<<" ";
    }

    return 0;
}