#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define mod 1000000007
typedef unsigned long long ull;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string a, b;
    cin >> a >> b;
    //cout<<a<<" "<<b<<endl;
    //cout<<a.size()<<" "<<b.size()<<endl;
    
    vector<ull> counts(b.size(), 0);
    counts[b.size()-1] = (b[b.size()-1] == '1');
    //cout<<b.size()-1<<" "<<counts[]<<endl;
    for(size_t i = b.size()-1; i > 0; i--){
        //cout<<b[i-1]<<endl;
        counts[i-1] = counts[i] + (b[i-1] == '1');
        //cout<<counts[i-1]<<endl;
    }
    
    ull sum = 0;
    ull power = 1;
    for(size_t i = 0; i < 314159+b.size(); i++){
        if(i > 0) power = (power * 2)%mod;
        int j = b.size()-i-1;
        if(i >= b.size())  j = 0;
        if(i < a.size()){
            if(a[a.size()-1-i] == '0'){
                sum = (sum + (counts[j]*power)%mod)%mod;
            }else{
                sum = (sum + ((314159+1-counts[j])*power)%mod)%mod;
            }
        }else if(i > 314159){
            //cout<<b.size()-i+314159<<endl;
            sum = (sum + ((counts[j]-counts[b.size()-i+314159])*power)%mod)%mod;
        }else{
            sum = (sum + (counts[j]*power)%mod)%mod;
            //cout<<j<<" "<<counts[j]<<endl;
        }
    }
    cout<<sum<<endl;
    
    return 0;
}
