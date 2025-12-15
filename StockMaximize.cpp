#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long profit(vector<int> price)
{
    int max = price[price.size() - 1];
    unsigned long long sum = 0;
    for(int i = price.size() - 2; i >= 0; i--){
        int current = price[i];
        if(current > max) max = current;
        sum += max - price[i];
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
        vector<int> price;
        for(int i = 0; i < n; i++){
            int tmp;
            cin >> tmp;
            price.push_back(tmp);
        }
        unsigned long long max = profit(price);
        cout<<max<<endl;
    }
    return 0;
}
