#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

ll miniMax(const vector<ll> &arr, const ll &p, const ll &q)
{
    vector<ll> b;
    ll mp = 0, mq = 1000000001;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] >= p && arr[i] <= q){ b.push_back(arr[i]);}
        if(arr[i] < p && arr[i] > mp) mp = arr[i];
        if(arr[i] > q && arr[i] < mq) mq = arr[i];
    }
    sort(b.begin(), b.end());
    ll mini = p;
    ll tmp = min(p - mp, b[0] - p);
    if(mp == 0) tmp = b[0] - p;
    else{
        if(mp + (b[0] - mp)/2 >= p){
            mini = mp + (b[0] - mp)/2;
            tmp = (b[0] - mp)/2;
        }
    }
    ll gap = tmp;
    for(int i = 1; i < b.size(); i++){
        //cout<<b[i]<<endl;
        tmp = (b[i] - b[i-1])/2;
        if(tmp > gap){
            mini = b[i-1] + tmp;
            gap = tmp;
        }
    }
    ll qq = q;
    tmp = min(q-b[b.size()-1], mq-q);
    if(mq == 1000000001) tmp = q - b[b.size()-1];
    else{
        if(b[b.size()-1] + (mq - b[b.size()-1])/2 <= q){
            tmp = (mq - b[b.size()-1])/2;
            qq = b[b.size()-1] + (mq - b[b.size()-1])/2;
        }
    }
    if(tmp > gap){
        mini = qq;
        gap = tmp;
    }
    return mini;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<ll> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    ll p, q;
    cin >> p >> q;
    cout<<miniMax(arr, p, q)<<endl;
    return 0;
}
