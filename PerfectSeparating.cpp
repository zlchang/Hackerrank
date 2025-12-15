#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
int m = 0, ma = 0, mb = 0;
ull count(string str, vector<char> &target, int im, int ia, int ib, vector<vector<ull>> &dp)
{
    //cout<<"ia: "<<ia<<" ib: "<<ib<<" im: "<<im<<endl;
    ull res = 0;
    if(im == m){ 
        //for(auto i : target) cout<<i; cout<<endl;
        //cout<<dp[m-1][str.size()-1]<<endl;
        return dp[m-1][str.size()-1];
    }
    if(ia < ma){
        target[im] = 'a';
        //cout<<"ia: "<<ia<<" im: "<<im<<endl;
        
        for(int is = 0; is <= im+1; is++){
            dp[im][im+is] = 0;
        }
        if(im == 0){
            if(str[im] == 'a') dp[im][im] = 1;
        }else{
            if(str[im] == 'a' && dp[im-1][im-1]) dp[im][im] = 1;
        }
        for(int is = im+1; is <= 2*im; is++){
            if(target[is-im-1] == str[is]){
                dp[im][is] += dp[im][is-1];
            }
            if(str[is] == 'a'){
                dp[im][is] += dp[im-1][is-1];
            }
            //cout<<"a: "<<im<<" "<<is<<" "<<dp[im][is]<<endl;
        }
        if(str[2*im+1] == 'a') dp[im][2*im+1] = 2*dp[im][2*im];
        //cout<<"a: "<<im<<" "<<2*im+1<<" "<<dp[im][2*im+1]<<endl;
        ull s = 0;
        for(int i = 0; i <= im; i++){
            s += dp[i][im];
        }
        if(s) res += count(str, target, im+1, ia+1, ib, dp);
    }
    if(ib < mb){
        target[im] = 'b';
        //cout<<"ib: "<<ib<<" im: "<<im<<endl;      
        for(int is = 0; is <= im+1; is++){
            dp[im][im+is] = 0;
        }
        if(im == 0){
            if(str[im] == 'b') dp[im][im] = 1;
        }else{
            if(str[im] == 'b' && dp[im-1][im-1]) dp[im][im] = 1;
        }
        for(int is = im+1; is <= 2*im; is++){
            if(target[is-im-1] == str[is]){
                dp[im][is] += dp[im][is-1];
            }
            if(str[is] == 'b'){
                dp[im][is] += dp[im-1][is-1];
            }
            //cout<<"b: "<<im<<" "<<is<<" "<<dp[im][is]<<endl;
        }
       if(str[2*im+1] == 'b') dp[im][2*im+1] = 2*dp[im][2*im];
       //cout<<"b: "<<im<<" "<<2*im+1<<" "<<dp[im][2*im+1]<<endl;
       ull s = 0;
       for(int i = 0; i <= im; i++){
        s += dp[i][im];
       }
       if(s) res += count(str, target, im+1, ia, ib+1, dp);
    }
    return res;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string str;
    cin >> str;
    int n = str.size();
    int cnta = 0, cntb = 0;
    for(int i = 0; i < n; i++){
        if(str[i] == 'a') cnta++;
        else cntb++;
    }
    if(n%2 || cnta%2 || cntb%2) cout<<"0"<<endl;
    else{
        m = n/2; ma = cnta/2; mb = cntb/2;
        vector<char> target(m);
        vector<vector<ull>> dp(m);
        for(int i = 0; i < m; i++){
            vector<ull> tmp(n,0);
            dp[i] = tmp;
            //cout<<i<<" "<<n<<" "<<dp[i][n]<<endl;
        }
        cout<<count(str, target, 0, 0, 0, dp)<<endl;
    }
    return 0;
}
