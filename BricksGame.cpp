#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

ull payoff(vector<ull> brick)
{
    size_t n = brick.size();
    vector<ull> remain(n);
    vector<ull> sum(n);
    sum[0] = brick[n-1];
    for(size_t i = 1; i < n; i++){
        sum[i] = sum[i-1]+brick[n-1-i];
    }
    for(size_t i = 0; i < n; i++){
        if(i <= 2) remain[i] = sum[i];
        else{
            remain[i] = max(sum[i]-remain[i-1], sum[i]-remain[i-2]);
            remain[i] = max(sum[i]-remain[i-3], remain[i]);
        }
    }       
    return remain[n-1];   
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<ull> brick(n);
        for(int i = 0; i < n; i++){
            cin  >> brick[i];
        }
        cout<<payoff(brick)<<endl;
    }
    return 0;
}
