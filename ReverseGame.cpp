#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        ull n, k;
        cin >> n >> k;
        ull h = n/2;
        ull p = 0;
        if(k < h){
            p = 1 + 2*k;
        }else{
            p = 2*(n - 1 - k);
        }
        cout<<p<<endl;
    }
    return 0;
}
