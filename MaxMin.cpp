#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main() {
    int N, K, unfairness = INT_MAX;
    cin >> N >> K;
    int list[N];
    for (int i=0; i<N; i++)
        cin >> list[i];
    
    /** Write the solution code here. Compute the result, store in  the variable unfairness --
    and output it**/
    qsort(list, N, sizeof(int), compare);
    const int M = N - K + 1;
    int unfair[M];
    for(int i = 0; i < M; i++){
        unfair[i] = list[i+K-1] - list[i];
    }
    unfairness = unfair[0];
    for(int i = 1; i < M; i++){
        if(unfair[i] < unfairness) unfairness = unfair[i]; 
    }
    
    cout << unfairness << "\n";
    return 0;
}
