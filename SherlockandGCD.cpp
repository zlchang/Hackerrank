#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long gcd(long a, long b)
{
    if(b == 0) return a;
    return gcd(b, a%b);
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n;
        cin >> n;
        vector<long> test;
        int tgcd = 0;
        for(int i = 0; i < n; i++){
            long tmp;
            cin >> tmp;
            tgcd = gcd(tgcd, tmp);
        }
        if(tgcd == 1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
