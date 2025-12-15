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
    int sum1 = 0;
    int sum2 = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int num;
            cin >> num;
            if(i == j) sum1 += num;
            if(i + j == n - 1) sum2 += num;
        }
    }
    int diff = sum1 > sum2 ? sum1-sum2 : sum2 -sum1;
    cout<<diff<<endl;
    return 0;
}
