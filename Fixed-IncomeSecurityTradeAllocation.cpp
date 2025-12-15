#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct portfolio{
    string id;
    int order;
    int alloc;
};
bool compareById(portfolio a, portfolio b){
    return a.id < b.id;
}
bool compareByOrder(portfolio a, portfolio b){
    if(a.order < b.order) return true;
    if(a.order == b.order) return compareById(a, b);
    return false;
}
bool tradable(int alloc, int order, int min, int incr)
{
   int left = order - alloc;
   if(left == 0 || (left >= min && (left - min)%incr == 0)) return true;
   return false;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    int min, incr, avail;
    cin >> min >> incr >> avail;
    vector<portfolio> porto;
    while(t--){
        string id;
        int order;
        cin >> id >> order;
        portfolio pp;
        pp.id = id;
        pp.order = order;
        pp.alloc = 0;
        porto.push_back(pp);
    }
    sort(porto.begin(), porto.end(), compareByOrder);
    int total = 0;
    for(vector<portfolio>::iterator p = porto.begin(); p != porto.end(); p++){
        total += p->order;
    }
    for(vector<portfolio>::iterator p = porto.begin(); p != porto.end(); p++){
        int alloc = 0.;
        int order = p->order;
        double palloc = (order + 0.)/(total + 0.)*avail;
        //cout<<palloc<<endl;
        if(palloc < min){
            if(palloc > (min+0.)/2){
                int talloc = min;
                if(tradable(talloc, order, min, incr))
                    alloc = min;
            }
        }else{ 
            if(palloc >= order){
               alloc = order;
            }else{
                int nincr = floor((palloc-min)/incr);
                //cout<<"n: "<<nincr<<endl;
                while(nincr >= 0){
                    int talloc = min + nincr*incr;
                    if(tradable(talloc, order, min, incr)){
                        alloc = talloc;
                        break;
                    }
                    nincr--;
                }
            }
        }
        total -= order;
        avail -= alloc;
        p->alloc = alloc;
        //cout<<total<<" "<<avail<<endl;
        //cout<<p->id<<" "<<alloc<<endl;
    }
    sort(porto.begin(), porto.end(), compareById);
    for(vector<portfolio>::iterator p = porto.begin(); p != porto.end(); p++){
        printf("%s %d\n", p->id.c_str(), p->alloc);
    }
    return 0;
}
