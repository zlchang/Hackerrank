#include <cmath>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

float distance(vector<int> y, int n)
{
    unordered_map<int, int> counter;
    sort(y.begin(), y.end());
    for(int i = 0; i < n; i++){
        if(counter.find(y[i]) == counter.end()){
            counter.insert(make_pair(y[i], n - i));
        }
    }
    float sum = 0.;
    for(size_t i = 0; i < n; i++){
        int v = y[i];
        int m = counter[v];
//        cout<<v<<" "<<m<<endl;
        sum += (n + 1.0)/(m + 1.0);
    }
    return sum;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    cin >> T;
    while(T--){
        int n;
        cin >> n;
        vector<int> y(n);
        for(int i = 0; i < n; i++){
            cin >> y[i];
        }
        float dis = distance(y, n);
        printf("%.2f\n", dis);
    }
    return 0;
}
