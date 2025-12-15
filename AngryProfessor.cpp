#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int N, K;
        cin >> N >> K;
        int counter = 0;
        for(int in = 0; in < N; in++){
            int tt;
            cin >> tt;
            if(tt <= 0) counter++;        
        }
        if(counter < K) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
        
    return 0;
}
