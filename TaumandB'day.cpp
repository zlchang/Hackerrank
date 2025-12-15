#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        long b, w;
        long x, y, z;
        cin >> b >> w;
        cin >> x >> y >> z;
        long cost;
        if(x < y){
            if(x+z < y) cost = b*x + (x+z)*w;
            else cost = b*x + w*y;
        }else{
            if(y+z < x) cost = b*(y+z) + y*w;
            else cost = b*x + w*y;
        }
        cout<<cost<<endl;
    }
    return 0;
}
