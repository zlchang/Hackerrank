#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void maxsub(vector<int> a, int &cm, int &ncm)
{
    cm = 0; ncm = 0;
//    size_t index = 0;
    int max = 0;
    int current = 0;
    for(size_t i = 0; i < a.size(); i++){
        if(a[i] > 0) ncm += a[i];
        if(current + a[i] >= 0){
          current += a[i];
        }else{
//            index = i+1;
            current = 0;
        }
        if(current > max) max = current;
    }
    cm = max;
    if(ncm == 0){
        int mx = a[0];
        for(int i = 0; i < a.size(); i++){
            if(a[i] > mx) mx = a[i];
        }
        cm = mx;
        ncm = mx;
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    while(T--){
        int n;
        cin >> n;
        vector<int> a;
        for(int i = 0; i < n; i++){
            int tmp;
            cin >> tmp;
            a.push_back(tmp);
        }
        int cm = 0,ncm = 0;
        maxsub(a, cm,ncm);
        cout<<cm<<" "<<ncm<<endl;
    }
    return 0;
}
