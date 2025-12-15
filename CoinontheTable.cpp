#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool inside(int i, int j, int n, int m)
{
    if(i < 0 || i >= n || j < 0 || j >= m) return false;
    return true;
}
int minOperation(vector<vector<char>>cell, const int n, const int m, int k)
{
    int prev[n][m];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            prev[i][j] = -1;
            
    prev[0][0] = 0;
    while(k > 0){
        int curr[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                vector<int> minOp;
                if(inside(i-1, j, n, m) && prev[i-1][j] != -1){
                    int op;
                    if(cell[i-1][j] == 'D') op = prev[i-1][j];
                    else op = prev[i-1][j]+1;
                    minOp.push_back(op);
                }
                if(inside(i, j-1, n, m) && prev[i][j-1] != -1){
                    int op;
                    if(cell[i][j-1] == 'R') op = prev[i][j-1];
                    else op = prev[i][j-1]+1;
                    minOp.push_back(op);
                }
                if(inside(i+1, j, n, m) && prev[i+1][j] != -1){
                    int op;
                    if(cell[i+1][j] == 'U') op = prev[i+1][j];
                    else op = prev[i+1][j]+1;
                    minOp.push_back(op);
                }
                if(inside(i, j+1, n, m) && prev[i][j+1] != -1){
                    int op;
                    if(cell[i][j+1] == 'L') op = prev[i][j+1];
                    else op = prev[i][j+1]+1;
                    minOp.push_back(op);
                }
                if(cell[i][j] == '*' && prev[i][j] != -1) minOp.push_back(prev[i][j]);
                if(!minOp.empty()) curr[i][j] = *min_element(minOp.begin(), minOp.end());
                else curr[i][j] = -1;
                //cout<<"k " <<k <<" i "<<i<<" j "<<j<<" curr "<<curr[i][j]<<endl;
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                prev[i][j] = curr[i][j];
            }
        }
        k--;
    }
    int numOp = -1;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(cell[i][j] == '*') numOp = prev[i][j];
        }
    }
    return numOp;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,m,k;
    cin >> n >> m >> k;
    vector<vector<char>> cell(n);
    for(int i = 0; i < n; i++){
        vector<char> row(m);
        cell[i] = row;
        for(int j = 0; j < m; j++){
            cin >> cell[i][j];
        }
    }
    int minOp = minOperation(cell, n, m, k);
    cout<<minOp<<endl;
    return 0;
}
