#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ull r, c;
    cin >> r >> c;
    ull n = (r-1)/2*10 + 2*(c-1) + (1 - r%2);
    cout<<n<<endl;
    return 0;
}
