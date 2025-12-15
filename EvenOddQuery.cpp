#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i =0 ; i < n; i++){
        int tmp;
        cin >> tmp;
        arr.at(i) = tmp;
    }
    int q; 
    cin >> q;
    while(q--){
        int x,y;
        cin >> x >> y;
        if(x > y) cout<<"Odd"<<endl;
        else if(arr.at(x-1) % 2) cout<<"Odd"<<endl;
        else{
            if(x+1 <= y && arr.at(x) == 0) cout<<"Odd"<<endl;
            else cout<<"Even"<<endl;
        }
        
    }
    return 0;
}
