#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = b;
    b = a;
    a = tmp;
}
void quicksort(vector<int> &arr, int start, int end)
{
    //cout<<start<<" "<<end<<endl;
    int j = start;
    int pivot = end - 1;
    for(int i = start; i < pivot; i++){
        if(arr[i] < arr[pivot]){
          swap(arr[i], arr[j]);
          j++;
        }
    }
    swap(arr[pivot], arr[j]);
    for(int k = 0; k < arr.size(); k++){
        cout<<arr[k]<<" ";
    }
    cout<<endl;
    
    if(j - start > 1) quicksort(arr, start, j);
    if(end - j > 2) quicksort(arr, j+1, end);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    quicksort(arr, 0, n);
    return 0;
}
