#include <iostream>
#include <string>
using namespace std;

int main(){

    string mystring;
    cout<<"insert your string: ";
    cin>>mystring;
    int len = mystring.length();

    for (int i=0;i<len;i++){
        int j=i;

        while (j>0 && mystring[j]<mystring[j-1]){
            swap(mystring[j], mystring[j-1]);
            j-=1;
        }

    }
    cout<<mystring<<endl;

    return 0;
}