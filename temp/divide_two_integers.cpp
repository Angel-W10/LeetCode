#include <iostream>

using namespace std;

int divide(int dividend, int divisor) {

    bool neg = false;

    if(dividend==divisor){
        return 1;
    }
    if(dividend<divisor){
        return 0;
    }

    if (dividend<0 || divisor<0){
        neg = true;
    }
    if (dividend<0){
        dividend = 0 - dividend;
    }
    if (divisor<0){
        divisor = 0 - divisor;
    }

    int counter = 0;

    while (dividend>divisor){
        dividend -= divisor;
        counter++;
    }

    if (neg){
        return -counter;
    }
    return counter;

}



int main(){


    int sol = divide(1, 1);
    cout<<sol<<endl;

    return 0;
}