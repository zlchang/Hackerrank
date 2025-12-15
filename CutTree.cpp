#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int N, K;
vector<vector<int>> edges(50);
unsigned long long f[50][50+1];
bool flag[50];
void depthfirst(int v)
{
    //cout<<"v = "<<v<<endl;
    flag[v-1] = true;
    vector<int> child;
    for(int i = 1; i <= edges[v-1].size(); i++){
        int c = edges[v-1][i-1];
        //cout<<"c = "<<c<<" flag: "<<flag[c-1]<<endl;
        if(!flag[c-1]) child.push_back(c);
    }
    const int L = child.size();
    unsigned long long dp[L+1][K+1];
    for(int i = 0; i <= L; i++)
        for(int j = 0; j <= K; j++)
            dp[i][j] = 0;
    dp[0][0] = 1;
    for(int i = 1; i <= L; i++){
        int c = child[i-1];
        depthfirst(c);
        for(int k = 0; k <= K; k++){
            if(k > 0) dp[i][k] = dp[i-1][k-1];
            for(int l = 0; l<= k; l++){
                dp[i][k] += dp[i-1][k-l]*f[c-1][l];
            }
        }
    }
    for(int i = 0; i <= K; i++){
        f[v-1][i] = dp[L][i];
        //cout<<v<<" "<<i<<" "<<f[v-1][i]<<endl;
    }
    //cout<<v<<endl;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    cin >> N >> K;
    int a, b;
    while(cin >> a >> b){
        edges[a-1].push_back(b);
        edges[b-1].push_back(a); 
    }
    for(int i = 0; i < N; i++)
        flag[i] = false;
    /*for(int i = 0; i < 50; i++){
        for(int j = 0; j <= 50; j++){
            f[i][j] = 0;
            if(j == 0) f[i][j] = 1;
        }
    }*/
    depthfirst(1);
    unsigned long long res = 0;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < K; j++)
            res += f[i][j];
    res += f[0][K]+1;
    cout<<res<<endl;
    return 0;
}
