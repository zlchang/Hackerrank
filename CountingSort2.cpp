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
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    const int m = 100;
    int count[m] = {0};
    for(int i = 0; i < n; i++){
        count[arr[i]] ++;
    }
    for(int i = 0; i < m; i++){
        for(int j = 0; j < count[i]; j++){
            cout<<i<<" ";
        }
    }
    cout<<endl;
    return 0;
}
