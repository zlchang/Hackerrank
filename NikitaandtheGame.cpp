#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;

ull points(vector<ull> &sum, ull is, ull id)
{
    ull tot = sum[id];
    tot -= sum[is];
    //cout<<is<<" sum: "<<sum[is]<<" "<<id<<" sum: "<<sum[id]<<endl;
    if(tot % 2) return 0;
    if(id - is == 1) return 0;
    for(ull i = is+1; i <= id; i++){
        if(sum[i] - sum[is] == tot/2) return 1 + max(points(sum, is, i), points(sum, i, id));
    }
    return 0;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        ull n;
        cin >> n;
        vector<int> arr(n,0);
        vector<ull> sum(n+1,0);
        sum[0] = 0;
        for(ull i = 0; i < n; i++){
            cin >> arr[i];
            sum[i+1] = sum[i] + arr[i];
        }
        ull p = points(sum, 0, n);
        cout<<p<<endl;
    }
    return 0;
}
