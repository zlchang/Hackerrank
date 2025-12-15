#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
#define M 1000000007;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        ull n;
        cin >> n;
        n = n%M;
        ull sum = (n*n) % M;
        cout<<sum<<endl;
    }
    return 0;
}
