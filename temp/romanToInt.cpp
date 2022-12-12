#include <iostream>
#include <string>

using namespace std;

int get_val(char s){
    if (s == 'I'){
        return 1;
    }
    else if(s == 'V'){
        return 5;
    }
    else if(s == 'X'){
        return 10;
    }
    else if(s == 'L'){
        return 50;
    }
    else if(s == 'C'){
        return 100;
    }
    else if(s == 'D'){
        return 500;
    }
    else if(s == 'M'){
        return 1000;
    }
    else{
        return -1;
    }
}

int romanToInt(string s) {

    int len = s.length();
    int out = 0;

    for (int i = 0; i < len; i++){

        if (get_val(s[i]) < get_val(s[i+1])){
            out += get_val(s[i+1]) - get_val(s[i]);  
            i++;  
        }

        else{
            out = out + get_val(s[i]);
        }

    }
    return out;
}


int main(){

    string s = "LVIII";
    cout<<romanToInt(s);

    return 0;
}