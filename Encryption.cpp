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
    string s;
    cin >> s;
    size_t n = s.size();
    int i = 0;
    while(i*i < n){
        i++;
    };
    size_t j = i - 1;
    if(i*j < n){ j += 1;}
    if(i*j < n){ i += 1;}
    for(int ic = 0; ic < i; ic++){
        for(int ir = 0; ir < j; ir++)
        if(ir*i+ic < n) cout<<s.at(ir*i+ic);
        cout<<" ";
    }
    cout<<endl;
    return 0;
}
