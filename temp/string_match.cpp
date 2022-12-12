#include <iostream>
#include <string>
using namespace std;

int main(){

    string ref_string;
    string sample;

    cout<<"insert your reference string: ";
    cin>>ref_string;

    cout<<"enter your sample: ";
    cin>>sample;

    int ref_len = ref_string.length();
    int sample_len = sample.length();

    for (int i = 0;i<ref_len;i++){
        int j=0;

        if (ref_string[i]==sample[j]){
            j++;
        }
        
    }


    cout<<mystring<<endl;

    return 0;
}
