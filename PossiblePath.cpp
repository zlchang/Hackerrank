#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

ull gcd(ull a, ull b)
{  
    while(a%b != 0){
        ull tmp = b;
        b = a%b;
        a = tmp;
    }
    return b;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    cin >> T;
    while(T--){
        ull a , b, c, d;
        cin >> a >> b >> c >>d;
        if(gcd(a,b) == gcd(c, d)) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
