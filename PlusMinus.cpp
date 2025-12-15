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
    int pos = 0, neg = 0, zero = 0;
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        if(num > 0) pos++;
        else if(num == 0) zero++;
        else if(num < 0) neg++;
    }
    printf("%.3f\n", (pos+0.)/(n+0.));
    printf("%.3f\n", (neg+0.)/(n+0.));
    printf("%.3f\n", (zero+0.)/(n+0.));
    return 0;
}
