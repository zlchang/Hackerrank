#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
ull keys(int n)
{
    if(n <= 3) return 1;
    vector<ull> arr(n);
    arr[0] = 1;
    arr[1] = 1;
    arr[2] = 1;
    arr[3] = 2;
    for(int i = 4; i < n; i++){
        arr[i] = arr[i-1] + arr[i-4];
        //cout<<i<<" "<<arr[i]<<endl;
    }
    return arr[n-1];
}
bool prime(ull p)
{
    if(p == 2 || p == 3) return true;
    int i = 2;
    while(i*i <= p){
        if(p%i == 0) return false;
        i++;
    }
    return true;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        ull m = keys(n);
        ull count = 0;
        //cout<<m<<endl;
        for(ull i = 2; i <= m; i++){
            if(prime(i)) count++;
        }
        cout<<count<<endl;
    }
    return 0;
}
