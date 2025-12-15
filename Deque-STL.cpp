#include <iostream>
#include <deque> 
#include <algorithm>
using namespace std;
void printKMax(int arr[], int n, int k){
   //Write your code here.
   deque<int> tmp;
   for(int i = 0; i < k; i++){
     tmp.push_back(arr[i]);
   }
   int max = *(max_element(tmp.begin(), tmp.end()));
   cout<<max<<" ";
   for(int i = k; i < n; i++){
       //cout<<arr[i-k]<<" "<<arr[i]<<" "<<max<<endl;
       tmp.pop_front(); tmp.push_back(arr[i]);
       if(arr[i-k] == max && arr[i] < max){
           max = *(max_element(tmp.begin(), tmp.end()));
       }else if(arr[i] > max){
           max = arr[i];
       }
       cout<<max<<" "; 
   }
   cout<<endl;
}
int main(){
  
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
