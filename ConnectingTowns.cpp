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
        size_t n;
        cin >> n;
        vector<int> nr(n-1);
        for(size_t i = 0; i < n-1; i++){
            cin >> nr.at(i);
        }
        unsigned long long total = 1;
        for(size_t i = 0; i < n-1; i++){
           total = (total * nr.at(i))%1234567; 
        }
        cout<<total<<endl;
    }
    return 0;
}
