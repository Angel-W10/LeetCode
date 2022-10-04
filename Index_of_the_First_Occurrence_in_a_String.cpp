// index of the first occurence in a string

#include <iostream>
#include <string>

using namespace std;

int strStr(string haystack, string needle) {

    int counter = 0;
    bool match = false;
    int out = 0;
    int h = 0;
    int n = 0;

    while (h<haystack.length() && n < needle.length()){
        if(haystack[h]==needle[n]){
            h++;
            n++;
        }
        else{
            h=h-n+1;
            n=0;
        }
    }
    if (n=needle.length()){
        return h-n;
    }
    return -1;

}


int main(){
    string haystack = "leetcode", needle = "leeto";
    int out = strStr(haystack, needle);
    cout<<"out = "<<out<<endl;

    return 0;
}