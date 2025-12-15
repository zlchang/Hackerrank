#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t,n,c,m;
    cin>>t;
    while(t--){
        cin>>n>>c>>m;
        int answer=0;
        // Computer answer
        int nbuy = n/c;
        answer += nbuy;
        int wrap = nbuy;
        while(wrap >= m){
            wrap -= m - 1;
            answer += 1;
        }
        cout<<answer<<endl;
    }
    return 0;
}
