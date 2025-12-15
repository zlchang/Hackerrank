#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> vec;
    while(n--){
        int tmp;
        cin >> tmp;
        vec.push_back(tmp);
    }
    sort(vec.begin(), vec.end());
    for(size_t i = 0; i < vec.size(); i++){
        cout<<vec.at(i)<<" ";
    }
    cout<<endl;
    return 0;
}
