#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void largest_permutation(vector<int> &arr, int k)
{   
    vector<int> index(arr.size());
    for(size_t i = 0; i < arr.size(); i++){
        index[arr[i]-1] = i;
    }
    int n = arr.size();
    for(size_t i = 0; i < arr.size() && k > 0; i++){
//        cout<<i<<" arr[i]:"<<arr[i]<<" n:"<<n<<endl;
        if(arr[i] != n){
            int j = index[n-1];
            //cout<<arr[i]<<" "<<arr[j]<<" "<<n<<endl;
            //cout<<"swap: "<<i<<" "<<j<<endl;
            swap(arr[i], arr[j]);
            swap(index[arr[i]-1], index[arr[j]-1]);
            //cout<<arr[i]<<" "<<arr[j]<<" "<<n<<endl;
            k--;
        }
        n--;
    }
    for(size_t i = 0; i < arr.size(); i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,k;
    cin >> n >> k;
    vector<int> arr(n);
    
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    largest_permutation(arr, k);
    return 0;
}
