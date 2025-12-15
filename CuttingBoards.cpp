#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int MOD = 1000000007;
typedef unsigned long long ull;
typedef vector<int>::iterator VI;

int minCost(vector<int> xcost, vector<int> ycost)
{
    sort(xcost.begin(), xcost.end(), greater<int>());
    sort(ycost.begin(), ycost.end(), greater<int>());
    ull cost = 0;
    ull nx = 1, ny = 1;
    VI px = xcost.begin(), py = ycost.begin();
    while(px != xcost.end() && py != ycost.end()){
        if(*px > *py){
            cost += (nx*(*px))%MOD;
            cost %= MOD;
            ny++;
            px++;
        }else{
            cost += (ny*(*py))%MOD;
            cost %= MOD;
            nx++;
            py++;
        }
    }
    if(px != xcost.end()){
        while(px != xcost.end()){
            cost += (nx*(*px))%MOD;
            cost %= MOD;
            px++;
        }
    }else{
        while(py != ycost.end()){
            cost += (ny*(*py))%MOD;
            cost %= MOD;
            py++;
        }
    }
    return cost;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int m, n;
        cin >> m >> n;
        vector<int> ycost(m-1), xcost(n-1);
        for(int i = 0; i < m-1; i++){
            cin >> ycost[i];
        }
        for(int i = 0; i < n-1; i++){
            cin >> xcost[i];
        }
        cout<<minCost(xcost, ycost)<<endl;
    }
    return 0;
}
