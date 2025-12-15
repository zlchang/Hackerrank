#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
void insertionSort(vector <int>  ar) {
    for(size_t i = 1; i < ar.size(); i++){
        int e = ar[i];
        size_t j = i;
        while(j-- && e < ar[j]){
            ar[j+1] = ar[j];
            for(size_t k = 0; k < ar.size(); k++){
                cout<<ar[k]<<" ";
            }
            cout<<endl;
        }
        ar[j+1] = e;
        if(j+1 != i){
            for(size_t k = 0; k < ar.size(); k++){
                    cout<<ar[k]<<" ";
            }
            cout<<endl;
        }
        
    }
}
int main(void) {
   vector <int>  _ar;
   int _ar_size;
cin >> _ar_size;
for(int _ar_i=0; _ar_i<_ar_size; _ar_i++) {
   int _ar_tmp;
   cin >> _ar_tmp;
   _ar.push_back(_ar_tmp); 
}

insertionSort(_ar);
   
   return 0;
}
