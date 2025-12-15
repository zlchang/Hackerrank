#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool find(vector<int> a, vector<int> b, int k)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for(size_t i = 0; i < a.size(); i++){
        //cout<<a[i]<<" "<<b[a.size() - 1 -i]<<endl;
       if(k - a[i] > b[a.size() - 1 - i]) return false;
    }
    
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        vector<int> b(n);
        for(int i = 0; i < 2*n; i++){
            if(i < n) cin >> a[i];
            else cin >> b[i - n];
        }
        bool result = find(a, b, k);
        if(result) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
