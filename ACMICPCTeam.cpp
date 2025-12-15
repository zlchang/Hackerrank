#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, M;
    cin >> N >> M;
    vector<string> topic;
    for(int i = 0; i < N; i++){
        string tmp;
        cin >> tmp;
        topic.push_back(tmp);
    }
    int max = 0;
    int cnt = 0;
    for(size_t i = 0; i < topic.size(); i++){
        string ti = topic.at(i);
        for(size_t j = i+1; j < topic.size(); j++){
            string tj = topic.at(j);
            int tcnt = 0;
            for(int k = 0; k < M; k++){
                char ib = ti.at(k);
                char jb = tj.at(k);
                if(ib == '1' || jb == '1') tcnt++;
            }
            if(tcnt > max){
                max = tcnt;
                cnt = 1;
            }else if(tcnt == max){
                cnt++;
            }
        }
    }
    cout<<max<<endl;
    cout<<cnt<<endl;
    return 0;
}
