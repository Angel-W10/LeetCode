#include <iostream>
#include <string>
#include <stack>

using namespace std;



bool isValid(string s){

    stack<char> mystack;

    for (int i=0;i<s.length();i++){
        if (!mystack.empty()){
            if (mystack.top() == '(' && s[i]==')'  ||  mystack.top() == '[' && s[i]==']'  ||  mystack.top() == '{' && s[i]=='}'){
                mystack.pop();
                continue;
            }  
        }
        mystack.push(s[i]);
    }
    if (mystack.empty()){
        return true;
    }
    return false;

}



int main(){

    string s = "([)]";

    cout<<s<<endl;

    cout<<isValid(s)<<endl;


    return 0;
}