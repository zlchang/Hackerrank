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
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        int cntr = 0;
        int tmp = num;
        while(tmp){
            int digit = tmp%10;
            if(digit != 0 && num%digit == 0) cntr++;
            tmp = tmp/10;
        }
        cout<<cntr<<endl;
    }
    return 0;
}
