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
        ull n;
        cin >> n;
        if(n%2){
            cout<<"0"<<endl;
        }else{
            ull m = n/2;
            ull counter = 0;
            ull i = 1;
            while(i*i < m){
               if(m%i == 0) counter++;
               i++;
            }
            counter *= 2;
            if(i*i == m) counter += 1;
            cout<<counter<<endl;
        }
            
    }
    return 0;
}
