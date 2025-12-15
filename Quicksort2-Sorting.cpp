#include <bits/stdc++.h>
using namespace std;

void quickSort(vector <int> &arr) {
   // Complete this function
 
   vector<int> smaller;
   vector<int> larger;
   int pivot = arr[0];
   for(size_t i = 1; i < arr.size(); i++){
    if(arr[i] < pivot) smaller.push_back(arr[i]);
    else larger.push_back(arr[i]);
   }
   if(smaller.size() > 1) quickSort(smaller);
   if(larger.size() > 1) quickSort(larger);
        
   for(size_t i = 0; i < arr.size(); i++){
     if(i < smaller.size())
       arr[i] = smaller[i];
     else if(i == smaller.size())
         arr[i] = pivot;
     else      
       arr[i] = larger[i - smaller.size() - 1];             
   }
   if(arr.size() >= 2){
     for(size_t i = 0; i < arr.size(); i++){
       cout<<arr[i]<<" ";
     }
     cout<<endl;
   }
}


int main()
{
    int n;
    cin >> n;

    vector <int> arr(n);
    for(int i = 0; i < (int)n; ++i) {
        cin >> arr[i];
    }

    quickSort(arr);

    return 0;
}
