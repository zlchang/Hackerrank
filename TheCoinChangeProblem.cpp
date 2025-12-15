#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


unsigned long long coinChange(int c[], int m, int n)
{
    //number of coins
    const int mm = m + 1;
    //changes
    const int nn = n + 1;
    unsigned long long types[mm][nn];
    types[0][0] = 0;
    for(int im = 1; im <= m; im++){
        types[im][0] = 0;
    }
    for(int in = 1; in <= n; in++){
        types[0][in] = 0;
    }
    for(int in = 1; in <= n; in++){
        for(int im = 1; im <= m; im++){
            if(c[im-1] == in) types[im][in] = types[im-1][in] + 1;
            if(c[im-1] < in) types[im][in] = types[im][in-c[im-1]] + types[im-1][in];
            if(c[im-1] > in) types[im][in] = types[im-1][in];
            //cout<<"n:"<<in<<" m:"<<im<<" c:"<<c[im-1]
                //<<" t(m,n):"<<types[im][in]<<" t(m-1,n):"<<types[im-1][in];
            //if(c[im-1] < in)
                //cout<<" t(m,i-c)"<<types[im][in-c[im-1]];
            //cout<<endl;
        }
    }
    return types[m][n];
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, m;
    cin >> n >> m;
    int c[50] = {0};
    for(int i = 0; i < m; i++){
        cin >> c[i];
    }
    unsigned long long ntypes = coinChange(c, m, n);
    cout<<ntypes<<endl;
    return 0;
}
