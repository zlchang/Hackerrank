#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void swap(char &a, char&b)
{
    char t = a;
    a = b;
    b = t;
}
bool grid(char g[][100], int n)
{
    for(int i = 0; i < n; i++){
        for(int t = 0; t < n-1; t++){
            for(int j = 1; j < n; j++){
                if(g[i][j-1] > g[i][j]) swap(g[i][j-1], g[i][j]);
            }
        }
    }
    for(int i = 1; i < n; i++){
        for(int j = 0; j < n; j++){
            if(g[i-1][j] > g[i][j]) return false;
        }
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    while(T--){
        int n;
        cin >> n;
        char g[100][100];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++)
                cin >> g[i][j];
        }
        bool flag = grid(g, n);
        if(flag) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
        
    return 0;
}
