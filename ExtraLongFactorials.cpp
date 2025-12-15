#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    int result[300];
    for(int i = 0; i < 300; i++){
        result[i] = 0;
    }
    result[0] = 1;
    int cntr = 0;
    for(int i = 1; i <= n; i++){
        //cout<<"i = "<<i<<endl;
        int carry = 0;
        for(int j = 0; j <= cntr; j++){
            int tmp = i * result[j] + carry;
            result[j] = tmp%10;
            carry = tmp/10;
            //cout<<j<<" result: "<<result[j]<<" carry: "<<carry<<endl;
        }
        while(carry){
            cntr++;
            result[cntr] = carry%10;
            carry /= 10;
            //cout<<cntr<<" result: "<<result[cntr]<<" carry: "<<carry<<endl;
        }
        /*
        for(int i = cntr; i >= 0; i--){
        cout<<result[i];
        }
        cout<<endl;
        */
    }
    for(int i = cntr; i >= 0; i--){
        cout<<result[i];
    }
    cout<<endl;
    
    return 0;
}
