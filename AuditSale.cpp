#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct security{
    int price;
    int confidence;
    int diff;
};

bool compareByDiff(security a, security b)
{
    return a.diff > b.diff;
}
string maxSale(vector<security> sec, const int n, const int m, const int k)
{
  for(int i = 0; i < n; i++){
      sec[i].diff = (100 -  sec[i].confidence)*sec[i].price;
  }
  sort(sec.begin(), sec.end(), compareByDiff);
  
  double maxsum[n+1];
  maxsum[0] = 0.;
    
  vector<int> max;
  for(int i = 1; i <= n; i++){
    maxsum[i] = maxsum[i-1] + sec[i-1].price*100;
    max.push_back(sec[i-1].price*100);
    push_heap(max.begin(), max.end(), greater<int>());
    if(max.size() > k){
        pop_heap(max.begin(), max.end(), greater<int>());
        int pop = max.back();
        //cout<<i<<" "<<pop<<endl;
        maxsum[i] -= pop;
        max.pop_back();
    }
  }
  double wgtsum[n+1];
  wgtsum[n] = 0;
  vector<int> wgt;
  for(int i = n-1; i >= 0; i--){
      wgtsum[i] = wgtsum[i+1] + sec[i].price*sec[i].confidence;
      wgt.push_back(sec[i].price*sec[i].confidence);
      push_heap(wgt.begin(), wgt.end(), greater<int>());
      if(wgt.size() > m-k){
          pop_heap(wgt.begin(), wgt.end(), greater<int>());
          int pop = wgt.back();
          wgtsum[i] -= pop;
          wgt.pop_back();
      }
  }
    
  double sum = 0;
  for(int i = 0; i <= n; i++){
      sum = std::max(sum, maxsum[i]+wgtsum[i]);
  }
    
  double sale = sum;
  char result[20];
  sprintf(result, "%.0lf", sale);
  return string(result);
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, m, k;
    cin >> n >> m >> k;
    vector<security> sec(n);
    for(int i = 0; i < n ; i++){
        cin >> sec[i].price >> sec[i].confidence;
    }
    string sale = maxSale(sec, n, m, k);
    cout<<sale<<endl;
    return 0;
}
