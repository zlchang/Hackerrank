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
        int n;
        cin >> n;
        int sum = 1;
        for(int i = 0; i < n; i++){
            sum *= 2;
            sum %= 100000;
        }
        sum -= 1;
        cout<<sum<<endl;
    }
    return 0;
}
