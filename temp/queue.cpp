#include <iostream>

using namespace std;

int queue[100], n = 100, front = -1, rear = -1;

void insert(int val){
    if (rear == n-1){
        cout<<"overflow"<<endl;
    }
    else{
        if (front==-1){
        front=0;
        }
        rear++;
        queue[rear]=val;
    }
}
void remove(int val){
}