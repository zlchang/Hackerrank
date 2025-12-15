#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, k;
    cin >> n >> k;
    vector<int> imp;
    int luck = 0;
    while(n--){
        int l,t;
        cin >> l >> t;
        if(!t) luck += l;
        else imp.push_back(l);
    }
    sort(imp.begin(), imp.end(), std::greater<int>());
    for(int i = 0; i < imp.size(); i++){
        if(i < k) luck += imp[i];
        else luck -= imp[i];
    }
    cout<<luck<<endl;
    return 0;
}
