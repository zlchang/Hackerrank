#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


typedef unsigned long long ull;
#define module 1000000007

ull gridwalking(vector<int> x, vector<int> d, int m){
    const int Nd = x.size();
    const int Ns = m;
    /***nCr table***/
    ull comb[Ns][Ns+1];//comb(i,j) = comb(i-1,j)+combi-1,j-1)
    for(int j = 0; j < Ns+1; j++){
        if(j > 1) comb[0][j] = 0;
        else comb[0][j] = 1;
    }
    for(int i = 1; i < Ns; i++){
        comb[i][0] = 1;
        for(int j = 1; j < Ns+1; j++){
            comb[i][j] = comb[i-1][j] + comb[i-1][j-1];
            comb[i][j] %= module;
        }
    }
    //cout<<comb[12][6]<<endl;
    /***nCr table***/
    ull count[Nd][Ns];
    for(int i = 0; i < Nd; i++){
        const int Nx = d[i];
        ull step[Ns+1][Nx]; 
        for(int id = 0; id < Nx; id++){
            if(id == x[i]-1) step[0][id] = 1;
            else step[0][id] = 0;
            for(int im = 1; im <= Ns; im++)
                step[im][id] = 0;
        }
        for(int im = 1; im <= Ns; im++){
            for(int id = 0; id < Nx; id++){
                if(id-1 >= 0){
                    step[im][id] += step[im-1][id-1];
                    step[im][id] %= module;
                //cout<<im<<" "<<id<<" "<<step[im][id]<<" id-1:"<<step[im-1][id-1]<<endl;
                }
                if(id + 1 < Nx){
                    step[im][id] += step[im-1][id+1];
                    step[im][id] %= module;
                    //cout<<im<<" "<<id<<" "<<step[im][id]<<" id+1:"<<step[im-1][id+1]<<endl;
                }
            }
        }
        for(int s = 0; s < Ns; s++){
            count[i][s] = 0;
            for(int id = 0; id < Nx; id++){
                count[i][s] += step[s+1][id];
                count[i][s] %= module;
                //cout<<count[i][s]<<endl;
            }
        }
    }
    ull result[Nd][Ns];
    for(int i = 0; i < Nd; i++){
        for(int s = 0; s < Ns; s++){
            if(i == 0) result[i][s] = count[i][s];
            else{
                result[i][s] = result[i-1][s];
                for(int ks = 0; ks < s; ks++){
                    result[i][s] += (((result[i-1][s-ks-1]*count[i][ks])%module)*comb[s][ks+1])%module;
                    result[i][s] %= module;
                }
                result[i][s] += count[i][s];
                result[i][s] %= module;
            }
            //cout<<i<<" "<<s<<" "<<result[i][s]<<endl;
        }
    }
    return result[Nd-1][Ns-1];
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        vector<int> xx(n);
        vector<int> dd(n);
        for(int i = 0; i < n; i++){
            cin >> xx[i];
        }
        for(int i = 0; i < n; i++){
            cin >> dd[i];
        }
        //cout<<dd[0]<<endl;
        cout<<gridwalking(xx, dd, m)<<endl;;
    }
    return 0;
}
