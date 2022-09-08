#include <iostream>
#include <string>
using namespace std;

int main(){

    string mystring;
    cout<<"insert your string: ";
    cin>>mystring;

    int len = mystring.length();
    string min;

    for (int i=0; i<len;i++){
        min=i;
 
        for (int j=i+1; j<len;j++){

            if(mystring[j]<mystring[i]){

                min=j;
                swap(mystring[j], mystring[i]);

            }
        }
    }

    cout<<mystring<<endl;

    return 0;
}
