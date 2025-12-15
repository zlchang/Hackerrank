#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int toys(vector<int> arr)
{
    const int M = 10001;
    int w[M] = {0};
    for(size_t i = 0; i < arr.size(); i++){
        w[arr[i]]++;
    }
    int counter = 0;
    int iw = 0;
    while(iw < M){
        if(w[iw] != 0){
            iw += 5;
            counter++;
        }else{
            iw++;
        }
    }
    return counter;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    cout<<toys(arr)<<endl;
    return 0;
}
