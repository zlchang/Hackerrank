#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void find(int graph[][1000], int n, int m, int s, int distance[])
{
    int queue[1000];
    
    int is = s - 1;
    distance[is] = 0;
    int begin = 0;
    int end = 0;
    queue[begin] = is;
    end++;
    while(begin != end){
        is = queue[begin];
        begin++;
        for(int i = 0; i < n; i++){
            if(i == is) continue;
            if(graph[is][i] == 6) {
                //cout<<"s = "<<is<<" i =" <<i<<" distance:"<<distance[i]<<endl;
                if(distance[i] == 9999){
                    distance[i] = distance[is] + graph[is][i];
                    queue[end] = i;
                    end++;
                }
            }
        }
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        int graph[1000][1000];
        for(int i = 0; i < 1000; i++)
            for(int j = 0; j < 1000; j++)
                graph[i][j] = 0;
        for(int i  = 0; i < m; i++){
            int a, b;
            cin >> a >> b;
            //cout<<a<<" "<<b<<endl;
            graph[a-1][b-1] = 6;
            graph[b-1][a-1] = 6;
        }
        int s; 
        cin >> s;
        int distance[1000];
        for(int i = 0; i < 1000; i++){
            distance[i] = 9999;
        }
        distance[s-1] = 0;
        find(graph, n, m, s, distance);
        for(int i = 0; i < n; i++){
            if(distance[i] == 9999) distance[i] = -1;
            if(i != s-1) cout<<distance[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
