#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
struct node{
    int index;
    int rate;
};
bool compareByRate(node a, node b)
{
    return a.rate < b.rate;
}
ull minShares(vector<int> rates, vector<ull> shares)
{
    int n = rates.size();
    vector<node> nd(n);
    vector<vector<int>> index(n);
    for(int i = 0; i < n; i++){
        int low = i - 10;
        int high = i + 10;
        if(low < 0){
            low = 0;
        }
        if(high >= n){
            high = n-1;
        }
        //cout<<i<<" "<<low<<" "<<high<<endl;
        for(int j = low; j <= high; j++){
            if(rates[j] > rates[i]){
                index[i].push_back(j);
            }
        }
        nd[i].index = i;
        nd[i].rate = rates[i];
    }
    sort(nd.begin(), nd.end(), compareByRate);
    for(int ind = 0; ind < n; ind++){
        int i = nd[ind].index;
        ull curr = shares[i];
        int cr = rates[i];
        //cout<<i<<endl;
        for(int ii = 0; ii < index[i].size(); ii++){
            int j = index[i][ii];
            if(shares[j] <= curr){ 
                if(rates[j] > cr){  
                    shares[j] = curr + 1; 
            //cout<<j<<" "<<curr<<endl;
                }
            }
       }
    }
    ull sum = 0;
    for(int i = 0; i < n; i++){
        sum += shares[i]; 
        //cout<<shares[i]<<" ";
    }
    //cout<<endl;
    return sum;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<int> rates(n);
    for(int i = 0; i < n; i++){
        cin >> rates[i];
    }
    vector<ull> shares(n);
    for(int i = 0; i < n; i++){
        cin >> shares[i];
    }
    ull minTotal = minShares(rates, shares);
    cout<<minTotal<<endl;
    return 0;
}
