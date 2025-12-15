#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int h;
    cin >> h;
    int m;
    cin >> m;
    map<int, string>dictionary = {  
        {0, "twelve"}, {1, "zero"}, {2, "one"}, {3, "three"}, {4, "four"}, {5, "five"},
                                    {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"}, {10, "ten"},
                                    {11, "eleven"}, {12, "twelve"}, {13, "thirteen"}, {14, "fourteen"},{15, "quarter"},
                                    {16, "sixteen"}, {17, "seventeen"}, {18, "eighteen"}, {19, "nineteen"}, {20, "twenty"},
                                    {21, "twenty one"}, {22, "twenty two"}, {23, "twenty three"}, {24, "twenty four"}, {25, "twenty five"},
                                    {26, "twenty six"}, {27, "twenty seven"}, {28, "twenty eight"}, {29, "twenty nine"},{30, "half"}
   };
    if(m == 59) cout<<dictionary[60-m]<<" minute to "<<dictionary[(h+1)%12]<<endl;
    else if(m > 45) cout<<dictionary[60-m]<<" minutes to "<<dictionary[(h+1)%12]<<endl;
    else if(m == 45) cout<<dictionary[60-m]<<" to "<<dictionary[(h+1)%12]<<endl;
    else if(m > 30) cout<<dictionary[60-m]<<" minutes to "<<dictionary[(h+1)%12]<<endl;
    else if(m == 30) cout<<dictionary[m]<<" past "<<dictionary[h]<<endl;
    else if(m > 15) cout<<dictionary[m]<<" minutes past "<<dictionary[h]<<endl; 
    else if(m == 15) cout<<dictionary[m]<<" past "<<dictionary[h]<<endl;   
    else if(m > 1) cout<<dictionary[m]<<" minutes past "<<dictionary[h]<<endl;
    else if(m == 1) cout<<dictionary[m]<<" minute past "<<dictionary[h]<<endl;
    else if(m == 0) cout<<dictionary[h]<<" o' clock"<<endl;
        
    return 0;
}
