#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    multimap<int, int> order;
    for(int i = 1; i <= n; i++){
        int t, d;
        cin >> t >> d;
        int f = t+d;
        order.insert(make_pair(f, i));
    }
    for(multimap<int,int>::iterator p = order.begin(); p != order.end(); p++){
        cout<<p->second<<" ";
    }
    cout<<endl;
    return 0;
}
