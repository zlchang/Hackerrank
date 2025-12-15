#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b)
{
    while(a%b != 0){
        int r = a%b;
        a = b;
        b = r;
    }
    return b;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    while(T--){
        int l, b;
        cin >> l >> b;
        int d = gcd(l, b);
        int ld = l / d;
        int bd = b / d;
        int n = ld * bd;
        cout<<n<<endl;
        
    }
    return 0;
}
