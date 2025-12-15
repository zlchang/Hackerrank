#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> arr(n);
    const int nn = n;
    char string[nn][10];
    for(int i = 0; i < n; i++){
        cin >> arr[i] >> string[i];
    }
    const int m = 100;
    int count[m] = {0};
    for(int i = 0; i < n; i++){
        count[arr[i]] ++;
    }
    vector<int> helper(m);
    helper[0] = count[0];
    for(int i = 1; i < m; i++){
        helper[i] = helper[i-1] + count[i];
    }
    char output[nn][10];
    
    for(int i = 0; i < n; i++){
        int pos = helper[arr[i]];
        if(i >= n/2) strcpy(output[pos-count[arr[i]]], string[i]);
        else strcpy(output[pos-count[arr[i]]], "-");
        count[arr[i]]--;
    }
    for(int i = 0; i < nn; i++){
        cout<<output[i]<<" ";
    }
    cout<<endl;
    return 0;
}
