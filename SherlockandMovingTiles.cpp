#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double l, s1, s2;
    cin >> l >> s1 >> s2;
    double diff = s2 - s1 + 0.;
    if(diff < 0) diff = -1*diff;
    unsigned long int n;
    cin >> n;
    for(unsigned long int i = 0; i < n; i++){
        double area;
        cin >> area;
        double length = sqrt(area);
        //x1 = t*(s1)+l;
        //x2 = t*(s2);
        //length = x1-x2 = l+(s1-s2)*sqrt(2.)/2*t;
        double t = (l-length)/diff*sqrt(2.0);
        printf("%.4lf\n", t);
    }
    return 0;
}
