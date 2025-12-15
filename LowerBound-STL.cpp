#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> vec;
    while(n--){
        int v;
        cin >> v;
        vec.push_back(v);
    }
    int m;
    cin >> m;
    while(m--){
        int u;
        cin >> u;
        vector<int>::iterator low = lower_bound(vec.begin(), vec.end(), u);
        int index = low - vec.begin() + 1;
        if(*low == u) cout<<"Yes ";
        else cout<<"No ";
        cout<<index<<endl;
    }
    return 0;
}
