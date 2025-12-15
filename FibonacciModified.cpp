#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<unsigned int> opr(vector<unsigned int> a, vector<unsigned int> b)
{
    vector<unsigned int> tmp;
    size_t na = a.size();
    //cout<<"na "<<na<<endl;
    size_t nb = b.size();
    //cout<<"nb "<<nb<<endl;
    const unsigned int N = 100;
    //cout<<N<<endl;
    unsigned long long r = 0;
    for(size_t i = 0; i < na+na; i++){
        unsigned long long s = r;
        for(size_t j = 0; j <= i && j < na; j++){
            if(i - j < na){ 
                s += a[j]*a[i-j];
                //cout<<"i " << i <<" j "<<j<<" a[j] "<<a[j]<<" a[i-j] "<<a[i-j]<<endl;
            }
        }
        unsigned int m = s % N;
        r = (s - m) / N;
        //cout<<i<<" s "<<s<<" r "<<r<<" m "<<m<<endl;
        tmp.push_back(m);
    }
    while(r > 0){
        unsigned int m = r % N;
        r = (r - m) / N;
        tmp.push_back(m);
    }
    
    r = 0;
    for(size_t i = 0; i < nb; i++){
        unsigned long long s = r;
        s += (tmp[i] + b[i]);
        //cout<<"tmp[i] "<<tmp[i]<<" b[i] "<<b[i]<<endl;
        unsigned int m = s % N;
        r = (s - m) / N;
        //cout<<"add " << i<<" s "<<s<<" r "<<r<<" m "<<m<<endl;
        tmp[i] = m;
    }
    size_t ib = nb;
    //cout<<nb<<" tmp[nb] "<<tmp[nb]<<endl;
    while(r > 0){
        unsigned long long s = r;
        s += tmp[ib];
        //cout<<"s "<<s<<endl;
        unsigned int m = s % N;
        r = (s - m) / N;
        if(ib < tmp.size()) tmp[ib] = m;
        else tmp.push_back(m);
        ib++;
    }
   
    bool flag = false;
    int cntr = 0;
    for(vector<unsigned int>::reverse_iterator rp = tmp.rbegin(); rp != tmp.rend(); rp++){
        if(*rp != 0 && flag == false) flag = true;
        if(flag) {cntr++; 
                 // cout<<*rp;
                 }
    }
    //cout<<endl;
    if(cntr < tmp.size()){
        vector<unsigned int> sum;
        for(int i = 0; i < cntr; i++){
            sum.push_back(tmp[i]);
        }
        return sum;
    }
    //cout<<endl;
    return tmp;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    unsigned int a,b;
    unsigned int n;
    cin >> a >> b >> n;
    vector<unsigned int> prev;
    prev.push_back(a);
    vector<unsigned int> curr;
    curr.push_back(b);
    
    if(n == 1) cout<<a<<endl;
    else{
        while(n >= 2){
            if(n == 2){
                //cout<<"size: "<<curr.size()<<endl;
                for(vector<unsigned int>::reverse_iterator p = curr.rbegin(); p != curr.rend(); p++){
                    if(p!=curr.rbegin() && *p < 10) cout<<"0"<<*p;
                    else cout<<*p;
                }
                cout<<endl;
            }
            else{
               vector<unsigned int> tmp = prev;
               prev = curr;
               curr = opr(curr, tmp);
                /*
                for(vector<unsigned int>::reverse_iterator p = curr.rbegin(); p != curr.rend(); p++){
                    if(p!=curr.rbegin() && *p < 10) cout<<"0"<<*p;
                    else cout<<*p;
                }
                cout<<endl;
                */
            }
            n--;
        }
    }
    
    return 0;
}
