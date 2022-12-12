#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(int x){
    if (x<0 || (x %10 == 0 && x!=0)){
        return false;
    }

    int rev = 0;

    while (x>rev){
        rev = rev * 10 + x%10;
        x = x/10;
    }

    return (x==rev || x == rev/10);

}

int main(){

    int x = 1212;

    cout<<isPalindrome(x);


    return 0;
}