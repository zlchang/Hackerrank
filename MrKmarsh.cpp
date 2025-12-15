#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int m, n;
    cin >> m >> n;
    vector<vector<int>> up(m);
    for(int i = 0; i < m; i++){
        vector<int> uh(n);
        up[i] = uh;
    }
    for(int j = 0; j < n; j++){
        up[0][j] = 0;
    }
    //
    vector<vector<int>> left(m);
    for(int i = 0; i < m; i++){
        vector<int> lh(n);
        left[i] = lh;
        left[i][0] = 0;
    }
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            char land;
            cin >> land;
            if(land == 'x'){
                up[i][j] = -1;
                left[i][j] = -1;
            }else if(land == '.'){
                if(i > 0){
                    up[i][j] = up[i-1][j] + 1;
                }
                if(j > 0){
                    left[i][j] = left[i][j-1] + 1;
                }
            }
            //cout<<i<<" "<<j<<" "<<" up: "<<up[i][j]<<" left: "<<left[i][j]<<endl;
        }
    }
    int count = 0;
    for(int i = m-1; i > 0; i--){
        for(int ja = n-1; ja > 0; ja--){
            if(left[i][ja] == -1) continue;
            for(int jb = ja-1; jb >= ja-left[i][ja]; jb--){
                //cout<<ja<<" "<<jb<<endl;
                int umin = up[i][ja] < up[i][jb] ? up[i][ja] : up[i][jb];
                //cout<<umin<<endl;
                for(int k = umin; k > 0; k--){
                    if(left[i-k][ja] - left[i-k][jb] != ja - jb) continue;
                    else{
                        int tmp = 2*(ja-jb+k);
                        if(tmp > count) count = tmp;
                        break;
                    }
                }
            }
        }
    }
    if(count == 0) cout<<"impossible"<<endl;
    else
        cout<<count<<endl;
    return 0;
}
