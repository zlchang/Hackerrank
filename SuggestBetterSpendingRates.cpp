#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
struct seq_t
{
    vector<vector<int>> seq;
};
struct income_t
{
    vector<int> spend;
    double income;
};
bool compareIncome(income_t a, income_t b)
{
    return a.income > b.income;
}
double getIncome(vector<int> spend, int p, int t, double r)
{
    const int Nt = t;
    double left[Nt];
    left[0] = 1;
    for(int i = 1; i < Nt; i++){
        left[i] = left[i-1]*(100. - spend[i-1]);
    }
    double rp[Nt+1];
    rp[0] = 1;
    for(int i = 1; i <= Nt; i++){
        rp[i] = rp[i-1]*(1 + r/100)/100;
    }
    double income[Nt];
    for(int i = 0; i < Nt; i++){
        income[i] = p*spend[i]*left[i]*rp[i+1];
    }
    double sum = 0;
    for(int i = 0; i < Nt; i++){
        sum += income[i];
    }
    return sum;
}
//typedef unsigned long long ull;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double r;
    int p, t, th;
    cin >> p >> r >> t >> th;
    //cout<<t<<endl;
    vector<int> s(t);
    for(int i = 0; i < t; i++)
        cin >> s[i];
    //cout<<t<<" "<<th<<endl;
    double income = getIncome(s, p, t, r);
    printf("%0.3lf\n", income);
    
    const int Nt = t;
    seq_t prev[601];
    seq_t curr[601];
    
    for(int ith = -th; ith <= th; ith++){
        vector<int> arr;
        if(s[0]+ith >= 100 || s[0]+ith < 0) continue;
        arr.push_back(s[0]+ith);
        //cout<<arr[0]<<endl;
        //comb[0][ith+th].seq.push_back(arr);
        prev[ith+th].seq.push_back(arr);
        //cout<<comb[0][ith+th].seq[0][0]<<endl;
    }
    int fth[Nt];
    for(int i = 0; i < t; i++){
        int ff = (i+1)*th;
        int bb = (t-i-1)*th;
        fth[i] = ff < bb ? ff : bb;
        //cout<<fth[i]<<endl;
    }
    for(int i = 1; i < t; i++){
        for(int nth = -th; nth <= th; nth++){
            for(int mth = -fth[i-1]; mth <= fth[i-1]; mth++){
                int sum = mth + nth;              
                if(sum > fth[i] || sum < -fth[i]) continue;
                for(int ic = 0; ic < prev[mth+i*th].seq.size(); ic++){
                    if(s[i]+nth >= 100 || s[i]+nth < 0) continue;
                    vector<int> arr = prev[mth+i*th].seq[ic];
                    arr.push_back(s[i]+nth);
                    curr[sum+(i+1)*th].seq.push_back(arr);
                }
            }
        }
        for(int mth = -fth[i-1]; mth <= fth[i-1]; mth++){
            prev[mth+i*th].seq.clear();
        }
        
        for(int mth = -fth[i]; mth <= fth[i]; mth++){
            prev[mth+(i+1)*th].seq = curr[mth+(i+1)*th].seq;
        }
        for(int mth = -fth[i]; mth <= fth[i]; mth++){
            curr[mth+i*th+th].seq.clear();
        }
    }
    vector<income_t> sincome;
    for(int i = 0; i < prev[t*th].seq.size(); i++){
        vector<int> ss = prev[t*th].seq[i];
        income_t tmp;
        tmp.spend = ss;
        tmp.income = getIncome(ss, p, t, r);
        sincome.push_back(tmp);          
    }
    sort(sincome.begin(), sincome.end(), compareIncome);
    int n = 3;
    if(sincome.size() < 3) n = sincome.size();
    for(int i = 0; i < n; i++){
        printf("%0.3lf - ", sincome[i].income);
        for(int j = 0; j < sincome[i].spend.size(); j++){
            cout<<sincome[i].spend[j]<<" ";
        }
        cout<<endl;
    }
    
    return 0;
}
