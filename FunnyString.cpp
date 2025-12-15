#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        string str;
        cin >> str;
        bool flag = true;
        for(size_t is = 0; is <= str.size()/2 - 1; is++){
            size_t ia = is;
            size_t ib = str.size() - ia - 2;
            int va = (int) str.at(ia+1) - (int)str.at(ia);
            if(va < 0) va *= -1;
            int vb = (int) str.at(ib+1) - (int)str.at(ib);
            if(vb < 0) vb *= -1;
            if(va != vb) flag = false;
        }
        if(flag) cout<<"Funny"<<endl;
        else cout<<"Not Funny"<<endl;
    }
    return 0;
}
