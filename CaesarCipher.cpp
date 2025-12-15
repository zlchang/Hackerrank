#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, k;
    string str;
    cin >> n >> str >> k;
    for(size_t i = 0; i < str.size(); i++){
        int ascii = str.at(i);
        if(ascii <= 'Z' && ascii >= 'A') ascii = ((ascii - 'A')+k)%26 + 'A';
        if(ascii <= 'z' && ascii >= 'a') ascii = ((ascii - 'a')+k)%26 + 'a';
        str.at(i) = ascii;   
    }
    cout<<str<<endl;
    return 0;
}
