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
    vector<int> last;
    last.push_back(arr[0]);
    for(int i = 1; i < n; i++){
        if(arr[i]>(*(last.end()-1))) last.push_back(arr[i]);
        else{
            int bl = 0;
            if(arr[i] <= last[bl]) last[bl] = arr[i];
            else{
                int el = last.size()-1;
                //cout<<bl<<" "<<el<<endl;
                while(el - bl > 1){
                    int ml = (el + bl)/2;
                    if(arr[i] > last[ml]){
                        bl = ml;
                    }else{
                        el = ml;
                    }
                    //cout<<bl<<" "<<el<<" "<<ml<<endl;
                }
                last[el] = arr[i]; 
                //cout<<"i: "<<arr[i]<<" el: "<<el<<" "<<last[el]<<endl;
            }
        }
    }

    int maxlen = last.size();
    cout<<maxlen<<endl;
    return 0;
}
