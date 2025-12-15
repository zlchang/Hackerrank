#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long candy(vector<int> r)
{
    vector<int> cc(r.size());
    cc[0] = 1;
    for(size_t i = 1; i < r.size(); i++){
        if(r[i] > r[i-1]) cc[i] = cc[i-1] + 1;
        else cc[i] = 1;
    }
    for(int i = r.size() - 2; i >= 0; i--){
       if(r[i] > r[i+1]) cc[i] = cc[i+1]+1 > cc[i] ? cc[i+1]+1 : cc[i]; 
    }
    unsigned long long sum = 0;
    for(size_t i = 0; i < cc.size(); i++){
        sum += cc[i];
//        cout<<"cc["<<i<<"]: "<<cc[i]<<" sum: "<<sum<<endl;
    }
    return sum;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> rate;
    while(n--){
        int tmp;
        cin >> tmp;
        rate.push_back(tmp);
    }
    unsigned long long cc = candy(rate);
    cout<<cc<<endl;
    return 0;
}
