#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double profit(double usd, double eur, double gbp)
{
    double init = 1e+5;
    double quot = usd*eur*gbp;
    if(quot < 1){
        return init/quot - init;
    }
    return 0.;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    while(n--){
        double usd, eur, gbp;
        cin >> usd >> eur >> gbp;
        printf("%.0lf\n", floor(profit(usd,eur,gbp)));  
    }
    return 0;
}
