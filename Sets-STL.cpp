#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    set<int> st;
    while(n--){
        int x, y;
        cin >> x >> y;
        if(x == 1){
            st.insert(y);
        }else if(x == 2){
            if(st.find(y) != st.end()) st.erase(y);
        }else if(x == 3){
            if(st.find(y) != st.end()) cout<<"Yes"<<endl;
            else cout<<"No"<<endl;
        }
    }
    return 0;
}
