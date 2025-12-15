#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int operation(int n, vector<int> cho)
{
    int emax = *max_element(cho.begin(), cho.end());
    int emin = *min_element(cho.begin(), cho.end());
    const int nmax = emax+5;
    int step[nmax];
    for(int i = 0; i < nmax; i++){
        if(i == 0) step[i] = 0;
        else if(i == 1) step[i] = 1;
        else if(i == 2) step[i] = 1;    
        else if(i < 5){
            step[i] = min(step[i-1]+1, step[i-2]+1);
        }else if(i == 5){
            step[i] = 1;
        }else{
            step[i] = min(min(step[i-1]+1, step[i-2]+1), step[i-5]+1);
        }            
    }
    vector<int> sum(5);
    for(int is = 0; is < 5; is++){
        int total = 0;
        for(vector<int>::iterator p = cho.begin(); p != cho.end(); p++){
            //cout<<*p-emin+is<<" "<<step[*p-emin+is]<<endl;
            total += step[*p-emin+is];
        }
        sum[is] = total;
    }
    return *min_element(sum.begin(), sum.end());
}    
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> chocolate(n);
        for(int i = 0; i < n; i++){
            cin >> chocolate[i];
        }
        int oper = operation(n, chocolate);
        cout<<oper<<endl;
    }
    return 0;
}
