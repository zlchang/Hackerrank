#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
int findmedian(vector<int> arr, int start, int end)
{
    int a = start;
    //int b = 0;
    int pivot = arr[end-1];
    for(size_t i = start; i < end; i++){
        if(arr[i] < pivot){
            swap(arr[i], arr[a]);
            a++;
        }
        //a++;
    }
    if(a != end-1) swap(arr[a], arr[end-1]);
    if(a == arr.size()/2) return arr[a];
    else if (a < arr.size()/2) return findmedian(arr, a+1, end);
    else return findmedian(arr, start, a);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int median = findmedian(arr, 0, n);
    cout<<median<<endl;
    return 0;
}
