#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, T;
    cin >> N >>T;
    vector<int> width;
    for(int i = 0; i < N; i++){
        int ww;
        cin >> ww;
        width.push_back(ww);
    }
    for(int i = 0; i < T; i++){
        int enter, exit;
        cin >> enter >> exit;
        int min = width.at(enter);
        for(int iw = enter+1; iw <= exit; iw++){
            if(width.at(iw) < min) min = width.at(iw);
        }
        cout<<min<<endl;
    }
    return 0;
}
