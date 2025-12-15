#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
int mod = 1000000007;

ull Gfunc(vector<int> a)
{
    vector<ull> prev;
    vector<ull> curr;
    prev.push_back(a[0]);
    for(int i = 1; i < a.size(); i++){
        curr.push_back((prev[0]+a[i])%mod);
        for(int j = 1; j < i; j++){
            curr.push_back((prev[j-1]*a[i]+prev[j])%mod);
        }
        curr.push_back((prev[i-1]*a[i])%mod);
        prev.clear();
        prev = curr;
        curr.clear();
    }
    ull sum = 0;
    int counter = 1;
    for(auto v : prev){
        sum += (v*counter)%mod;
        sum %= mod;
        counter++;
        //cout<<v<<endl;
    }
    return sum;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    ull result = Gfunc(a);
    cout<<result<<endl;
    return 0;
}
