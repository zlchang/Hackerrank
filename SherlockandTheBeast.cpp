#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
vector<int> beast(int N)
{
    int n3 = 0;
    
    while((N-n3)%3 != 0 && n3 < N){
        n3 += 5;
    }
    if(n3 > N) return vector<int>(1, -1);
    vector<int> digit;
    for(int i = 0; i < N; i++){
        if(i < n3) digit.push_back(3);
        else digit.push_back(5);
    }
    return digit;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int N;
        cin >> N;
        vector<int>digit = beast(N);
        for(vector<int>::reverse_iterator rp = digit.rbegin(); rp != digit.rend(); rp++){
            cout<<(*rp);
        }
        cout<<endl;
    }
    return 0;
}
