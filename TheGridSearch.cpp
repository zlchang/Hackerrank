#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int R;
        int C;
        cin >> R >> C;
        vector<string> G(R);
        for(int G_i = 0;G_i < R;G_i++){
           cin >> G[G_i];
        }
        int r;
        int c;
        cin >> r >> c;
        vector<string> P(r);
        for(int P_i = 0;P_i < r;P_i++){
           cin >> P[P_i];
        }
        bool flag = false;
        for(size_t ig = 0; ig < R-r+1; ig++){
            size_t ii = ig;
            size_t jj = 0;
            size_t is = 0;
            while(is < C-c+1 && jj < r){
               size_t start = is;
               size_t js = 0;
               while(js < P[jj].size() && G[ii].at(start) == P[jj].at(js)){
                   start++;
                   js++;
//                   cout<<"in: is "<<is<<" ii "<<ii<<" start "<<start<<" jj "<<jj<<" js "<<js<<endl;
               }
//                   cout<<"out: is "<<is<<" ii "<<ii<<" start "<<start<<" jj "<<jj<<" js "<<js<<endl;
               if(js == P[jj].size()){
                  ii++;
                  jj++;
               }else{
                   ii = ig;
                   jj = 0;
                   is++;
               }
            }
            if(jj == r){
                flag = true;
            }
        }
        if(flag) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
