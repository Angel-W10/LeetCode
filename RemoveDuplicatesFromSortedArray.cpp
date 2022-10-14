// Given an integer array nums sorted in non-decreasing order, 
// remove the duplicates in-place such that each unique element appears only once. 
// The relative order of the elements should be kept the same.

// Since it is impossible to change the length of the array in some languages,
// you must instead have the result be placed in the first part of the array nums. 
// More formally, if there are k elements after removing the duplicates, 
// then the first k elements of nums should hold the final result. 
// It does not matter what you leave beyond the first k elements.

// Return k after placing the final result in the first k slots of nums.
#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    int c = 0;
    int val = nums[0];
        
    int len = nums.size();
    int last_num = len;
    
    for (int i = 0; i<len ; i++){
        int c = 0;
        int val = nums[c];

        if(nums[i+1]==val){

            for (int j = i+1 ; j < len-1 ; j ++){

                nums[j] = nums[j+1];

            }
            
            nums[last_num-1] = -1;
            last_num--;
            i--;            //checking if the element that replaced is equal to the val or not
            c++;           
        }
    }
    int k=0;
    for(int i=0;i<len;i++){
        if(nums[i]!=-1){
            k++;
        }
    }

    return k;    
        
}


int main(){


    vector<int> nums;
    nums.push_back(2);
    nums.push_back(2);
    nums.push_back(4);
    nums.push_back(3);
    nums.push_back(5);

    // for (int i = 0 ; i < nums.size() ; i++){
    //     cout<<nums[i]<<" ";
    // }

    // cout<<endl;

    int k = removeDuplicates(nums);

    cout<<k<<endl;

    return 0;
}