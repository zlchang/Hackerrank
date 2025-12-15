#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
#define MOD 1000000007
ull module(ull i, ull m)
{   
    if(m == 0) return 1;
    if(m%2) return ((i%MOD)*(module(i, m-1)%MOD))% MOD;
    return ((module(i, m/2)%MOD)*(module(i, m/2)%MOD))%MOD;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    //P(n+m-1, n) = (n+m-1)!/(n!*(m-1)!)
    ull t;
    cin >> t;
    while(t--){
        ull n,m;
        cin >> n >> m;
        ull p = n;
        if(n > m-1) p = m - 1;
        ull r = 1;
        for(ull i = 1; i <= p; i++){
            r = r * ((((n+m-1-p+i)%MOD) *module(i, MOD-2))%MOD);
            r = r % MOD;
        }

        cout<<r<<endl;
    }
    return 0;
}
