#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void squares(unsigned long long a, unsigned long long b)
{
    int counter = 0;
    unsigned long long i = 1;
    while(i*i <= b){
        if(i*i >=a){
            counter++;
        }
        i++;
    }
    cout<<counter<<endl;
}    

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        unsigned long long a, b;
        cin >> a >> b;
        squares(a, b);
    }
    return 0;
}
