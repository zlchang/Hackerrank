#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> vec;
    int n;
    cin >> n;
    while(n--){
        int tmp;
        cin >> tmp;
        vec.push_back(tmp);
    }
    int a;
    cin >> a;
    vec.erase(vec.begin()+a-1);
    int x, y;
    cin >> x >> y;
    vec.erase(vec.begin()+x-1, vec.begin()+y-1);
    
    cout<<vec.size()<<endl;
    for(size_t i = 0; i < vec.size(); i++){
        cout<<vec[i]<<" ";
    }
    cout<<endl;
    return 0;
}
