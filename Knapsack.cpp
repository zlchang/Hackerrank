#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int maxsum(vector<int> a, int k)
{
    vector<int> sum(k+1);
    sum[0] = 0;
    for(int i = 1; i <= k; i++){
        int tmax = 0;
        for(size_t ia = 0; ia < a.size(); ia++){
            if(a[ia] <= i){
                if(sum[i-a[ia]] + a[ia] > tmax) tmax = sum[i-a[ia]] + a[ia];
            }
        }
        sum[i] = tmax;
    }
    return sum[k];
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    while(T--){
        int n,k;
        cin >> n >> k;
        vector<int> a;
        for(int i = 0; i < n; i++){
            int tmp;
            cin >> tmp;
            a.push_back(tmp);
        }
        int sum = maxsum(a, k);
        cout<<sum<<endl;
    }
    return 0;
}
