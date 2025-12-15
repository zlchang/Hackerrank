#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    while(T--){
        int px, py, qx, qy;
        cin >> px >> py >> qx >> qy;
        int rx = 2*qx - px;
        int ry = 2*qy - py;
        cout<<rx<<" "<<ry<<endl;
    }
    return 0;
}
