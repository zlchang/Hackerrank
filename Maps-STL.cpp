#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    map<string, int> sheet;
    int n;
    cin >> n;
    while(n--){
        int q;
        string name;
        int mark;
        cin >> q ;
        if(q == 1)
            cin >> name >> mark;
        else cin >> name;
        if(q == 1){
            if(sheet.find(name) == sheet.end())
                sheet.insert(make_pair(name, mark));
            else sheet[name] += mark;
        }else if(q == 2){
            sheet.erase(name);
        }else if(q == 3){
            if(sheet.find(name) == sheet.end()) cout<<0<<endl;
            else cout<<sheet[name]<<endl;
        }
    }
    return 0;
}
