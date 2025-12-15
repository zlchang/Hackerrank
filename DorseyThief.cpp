#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
#include <unordered_map>
#include <algorithm>
using namespace std;

unsigned long long sell(multimap<unsigned long long, int, greater<unsigned long long>> value, int x)
{
    const int n = value.size() + 0;
    const int m = x + 1;
    int prev_weight[m];
    unsigned long long prev_profit[m];
    
    for(int j = 0; j < m; j++){
        prev_profit[j] = 0;
        prev_weight[j] = 0;
    }
    multimap<int, unsigned long long > weight;
    unordered_map<int, int> counter;
    for(multimap<unsigned long long, int>::iterator p = value.begin(); p != value.end(); p++){
        unsigned long long tv = p->first;
        int ta = p->second;
        if(ta > m) continue;
        if(counter.find(ta) == counter.end()){
            counter.insert(make_pair(ta, 0));
            weight.insert(make_pair(ta,tv));
        }
        else{
            if(counter[ta] < x/ta) weight.insert(make_pair(ta, tv));
            counter[ta]++;
        }
    }
    //cout<<"weight size: "<<weight.size()<<endl;
    for(multimap<int, unsigned long long> ::iterator p = weight.begin(); p != weight.end(); p++){
        int curr_weight[m];
        unsigned long long curr_profit[m];
        int ta = p->first;
        unsigned long long tv = p->second;
        vector<int> index;
        for(int j = 0; j < m; j++){
            if(ta <= j){
                if(prev_weight[j] < prev_weight[j-ta] + ta){
                    curr_weight[j] = prev_weight[j-ta] + ta;
                    curr_profit[j] = prev_profit[j-ta] + tv;
                    index.push_back(j);
                }else if(prev_weight[j] == prev_weight[j-ta] + ta){
                    curr_weight[j] = prev_weight[j];
                    curr_profit[j] = max(prev_profit[j], prev_profit[j-ta] + tv);
                    index.push_back(j);
                }
            }
//            cout<<i<<" "<<j<<" "<<ta<<" "<<tv<<" curr "<<curr_weight[j]<<" "<<curr_profit[j]<<" prev: "<<prev_weight[j]<<" "<<prev_profit[j]<<endl;
        }

        for(size_t j = 0; j < index.size(); j++){
            int k = index[j];
            prev_weight[k] = curr_weight[k];
            prev_profit[k] = curr_profit[k];
        }
    }
    if(prev_weight[m-1] == x) return prev_profit[m-1];
    else return 0;      
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, x;
    cin >> n >> x;
    multimap<unsigned long long, int, greater<unsigned long long>> value;
    for(int i = 0; i < n; i++){
        int ta;
        unsigned long long tv;
        cin >> tv >> ta;
        value.insert(make_pair(tv, ta));
    }
    unsigned long long profit = sell(value, x);
    if(profit == 0) cout<<"Got caught!"<<endl;
    else cout<<profit<<endl;
    return 0;
}
