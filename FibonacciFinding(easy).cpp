#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long fibonacci(unsigned long long fa, unsigned long long fb, unsigned long long num)
{
    unsigned long long mod = 1000000007;
    if(num == 0) return fa%mod;
    unsigned long long a[2][2] = {1, 1, 1, 0};
    unsigned long long b[2][2] = {1, 0, 0, 1};
    for(unsigned long long i = num; i > 1 ; i = i/2){
        if(i % 2 == 1){
        //cout<<"odd"<<endl;

        unsigned long long d[2][2] = {0, 0, 0, 0};
        for(int ib = 0; ib < 2; ib++){
            for(int jb = 0; jb < 2; jb++){
                for(int kk = 0; kk < 2; kk++){
                    d[ib][jb] += (a[ib][kk]*b[kk][jb])%mod;
                }
                
            }
         }
         for(int ia = 0; ia < 2; ia++){
             for(int ja = 0; ja < 2; ja++){
                 b[ia][ja] = d[ia][ja]%mod;
                 //cout<<ia<<" "<<ja<<" "<<d[ia][ja]<<endl;
             }
          }
        }
        //cout<<i<<endl;
        unsigned long long c[2][2] = {0, 0, 0, 0};
        for(int ib = 0; ib < 2; ib++){
            for(int jb = 0; jb < 2; jb++){
                for(int kk = 0; kk < 2; kk++){
                    c[ib][jb] += (a[ib][kk]*a[kk][jb])%mod;
                }
                
            }
        }
        for(int ia = 0; ia < 2; ia++){
            for(int ja = 0; ja < 2; ja++){
                a[ia][ja] = c[ia][ja]%mod;
                //cout<<ia<<" "<<ja<<" "<<c[ia][ja]<<endl;
            }
        }
    }
    unsigned long long e[2][2] = {0, 0, 0, 0};
    for(int ic = 0; ic < 2; ic++)
        for(int jc = 0; jc < 2; jc++)
            for(int kk = 0; kk < 2; kk++)
            e[ic][jc] += (a[ic][kk]*b[kk][jc])%mod;
    for(int ic = 0; ic <2; ic++)
        for(int jc = 0; jc < 2; jc++)
        a[ic][jc] = e[ic][jc]%mod;
    
    return ((a[1][0]*fb)%mod + (a[1][1]*fa)%mod)%mod;
    
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        unsigned long long a, b, num;
        cin >> a >> b >> num;
        unsigned long long fib = fibonacci(a, b, num);
        cout<<fib<<endl;
    }
    return 0;
}