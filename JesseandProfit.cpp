#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;
typedef long long ll;
void profit(const vector<ll> & arr, const ll &d, ll &start,  ll &end)
{
    if(arr.size() == 1) return;
    ll days = arr.size();
    unordered_map<ll, ll> prices;
    prices.insert(make_pair(arr[0], 0));
    for(ll i = 1; i < arr.size(); i++){
        if(prices.find(arr[i] - d) != prices.end()){
            ll j = prices[arr[i]-d];
            if(i-j < days){
                days = i - j;
                start = j+1;
                end = i+1;
            }
        }
        if(prices.find(arr[i]) != prices.end()){
            prices[arr[i]] = i;
        }else{
            prices.insert(make_pair(arr[i], i));
        }

    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ll n, d;
    cin >> n >> d;
    vector<ll> arr(n);
    for(ll i = 0; i < n; i++){
        cin >> arr[i];
    }
    while(d--){
        ll p;
        cin >> p;
        ll start = -1, end = -1;
        profit(arr, p, start, end);
        if(start == -1) cout<<start<<endl;
        else cout<<start<<" "<<end<<endl;
    }
    return 0;
}
