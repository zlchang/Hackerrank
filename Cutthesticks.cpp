#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N;
    cin >> N;
    vector<int> length;
    while(N--){
        int ll;
        cin >> ll;
        length.push_back(ll);
    }
    while(length.size() > 0){
        cout<<length.size()<<endl;
        int min = length.at(0);
        for(vector<int>::iterator it = length.begin(); it != length.end(); it++){
            if(*it < min) min = *it;
            //cout<<*it<<" min "<<min<<endl;
        }
        for(vector<int>::iterator it = length.begin(); it != length.end(); it++){
            //cout<<*it<<" cut "<<min<<endl;
           (*it) -= min;
            if((*it) == 0){
                length.erase(it);
                it--;
            }
        }
    }
    return 0;
}
