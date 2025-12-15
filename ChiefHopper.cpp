#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int initEnergy(const vector<int> &h)
{
    int n = h.size();
    int e = 0;
    for(int i = n-1; i >= 0; i--){
        e = (e+h[i])/2 + (e+h[i])%2;
    }
    return e;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> h(n);
    for(int i = 0; i < n; i++){
        cin >> h[i];
    }
    int en = initEnergy(h);
    cout << en <<endl;
    return 0;
}
