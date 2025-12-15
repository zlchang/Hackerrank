#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int v, n;
    cin >> v >> n;
    for(int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        if(v == tmp) cout<<i<<endl;
    }
    return 0;
}
