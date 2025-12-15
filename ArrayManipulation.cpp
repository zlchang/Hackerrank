#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ll n, m;
    cin >> n >> m;
    vector<ll> arr(n+1, 0);

    for(ll i = 0; i < m; i++){
        ll a, b, k;
        cin >> a >> b >> k;  
        arr[a-1] += k;
        arr[b] -= k;
    }
    ll max = 0;
    ll x = 0;
    for(ll i = 0; i <= n; i++){
        x += arr[i];
        if(x > max) max = x;    
    }
    cout<<max<<endl;
    
    return 0;
}
