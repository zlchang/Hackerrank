/* Sample program illustrating input/output */
#include<iostream>
using namespace std;
int compare(const void *a, const void* b)
{
    return *(int*)a - *(int *)b;
}
int main(void){
//Helpers for input and output

   int N, K;
   cin >> N >> K;
   int C[N];
    
   for(int i = 0; i < N; i++){
      cin >> C[i];
   }
    
   qsort(C, N, sizeof(int), compare);
   int result = 0;
   for(int i = N-1; i >=0 ; i--){
       result += (1+ (N-1-i)/K) * C[i];
   }
   cout << result << "\n";
   
   return 0;
}
