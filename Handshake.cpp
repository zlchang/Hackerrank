#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        ull sum = 0;
        for(int i = 0; i < n; i++){
            sum += i;
        }
        cout<<sum<<endl;
    }
    return 0;
}
