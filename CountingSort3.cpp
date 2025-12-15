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
    char string[10];
    for(int i = 0; i < n; i++){
        cin >> arr[i] >> string;
    }
    const int m = 100;
    int count[m] = {0};
    for(int i = 0; i < n; i++){
        count[arr[i]] ++;
    }
    vector<int> helper(m);
    helper[0] = count[0];
    cout<<helper[0]<<" ";
    for(int i = 1; i < m; i++){
        helper[i] = helper[i-1] + count[i];
        cout<<helper[i]<<" ";
    }
    cout<<endl;
    return 0;
}
