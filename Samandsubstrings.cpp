#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
#define mod 1000000007
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char num;
    vector<ull> ball;
    while(cin >> num){
        ball.push_back(num-'0');
    }
    size_t n = ball.size();
    ull sum = ball[0];
    ull res = ball[0];
    //ui res = ball[0];
    for(size_t i = 1; i < n; i++){
        sum = sum +(i*ball[i]+ball[i])%mod;
        sum %= mod;
        res = (res*10)%mod+sum;
        //res = (res*11)%mod + (i+1)*ball[i];
        res %= mod;
    }
    cout<<res<<endl;
    
    return 0;
}
