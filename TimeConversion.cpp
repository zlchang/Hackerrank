#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char time[2];
    int hh,mm,ss;
    if(scanf("%d:%d:%d%s", &hh, &mm, &ss, time) != 4){
        return 1;
    }
    if(strcmp(time, "AM") == 0){
      hh = hh%12;
    } 
    else if(strcmp(time,"PM") == 0){
        hh = (hh%12+12);
    } 
    printf("%.2d:%.2d:%.2d", hh, mm, ss);
    return 0;
}
