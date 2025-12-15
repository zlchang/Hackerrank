#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<string> str;
    int n;
    cin >> n;
    while(n--){
        string tmp;
        cin >> tmp;
        str.push_back(tmp);
    }
    cout<<str.at(0)<<endl;
    for(size_t i = 1; i < str.size()-1; i++){
        cout<<(str.at(i)).at(0);
        for(size_t j = 1; j < (str.at(i)).size()-1; j++){
            char a = (str.at(i)).at(j);
            char u = (str.at(i-1)).at(j);
            char d = (str.at(i+1)).at(j);
            char l = (str.at(i)).at(j-1);
            char r = (str.at(i)).at(j+1);
            if(a > u && a > d && a > l && a > r) cout<<"X";
            else cout<<a;
        }
        cout<<(str.at(i)).at((str.at(i)).size()-1);
        cout<<endl;
    }
    if(str.size() > 1) cout<<str.at(str.size()-1)<<endl;
    return 0;
}
