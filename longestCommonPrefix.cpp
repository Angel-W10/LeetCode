#include <iostream>
#include <vector>
#include <string>

using namespace std;

void longestCommonPrefix(vector<string>& strs) {
    string out = "";  

    for (int i = 0; i<strs.size();i++){
        cout<<strs[i]<<" ";
    }      
    // cout<<endl;
}


int main(){

    vector<string> strs;
    strs.push_back("Angel");
    strs.push_back("is");
    strs.push_back("amazing");

    longestCommonPrefix(strs);


    return 0;
}