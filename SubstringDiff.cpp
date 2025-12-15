#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int maxLength(const int &s, const string &a, const string &b)
{
    int length = 0;
    int n = a.size();
    int i = 0;
    for(int j = 0; j < b.size(); j++){
        vector<int> bad;
        int counter = 0;
        int start = 0;
        int m = 0;
        //cout<<i<<" "<<j<<" bad: "<<bad.size()<<endl;
        for(int l = 0; l < n - j; l++){
            m += (a[i+l] != b[j+l]);
            //cout<<a<<" "<<b<<endl;
            if(a[i+l] != b[j+l]){
                bad.push_back(l);
                //cout<<" push_back: "<<l<<endl;
            }

            if(m > s){
                length = max(length, l - start);
                //cout<<start<<" l: "<<l<<" m: "<<m<<endl;
                start = bad[counter] + 1;
                counter++;
                m--;
            }else{
               length = max(length, l - start + 1); 
            }
        }
        bad.clear();
    }
    return length;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int s;
        cin >> s;
        string a, b;
        cin >> a >> b;
        int L = max(maxLength(s, a, b), maxLength(s, b, a));
        cout<<L<<endl;
    }
    return 0;
}
