#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned int ui;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        ui n;
        cin >> n;
        vector<int> b(n);
        for(size_t i = 0; i < n; i++){
            cin >> b[i];
        }
        vector<ui> one(n);
        vector<ui> bb(n);
        one[0] = 0;
        bb[0] = 0;
        for(size_t i = 1; i < n; i++){
            one[i] = bb[i-1] + b[i-1] - 1;
            int diff = b[i] - b[i-1];
            if(diff < 0) diff = 0 - diff;
            bb[i] = one[i-1] + b[i]-1 > bb[i-1] + diff ? one[i-1] + b[i]-1 : bb[i-1] + diff;
        }
        ui res = one[n-1] > bb[n-1] ? one[n-1] : bb[n-1];
        cout<<res<<endl;
    }
    
    return 0;
}
