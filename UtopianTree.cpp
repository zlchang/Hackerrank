#include <iostream>
using namespace std;

int height(int n) {
    int cycle = 0;
    int hh = 1;
    while(cycle < n){
        if(cycle%2) hh += 1;
        else hh *= 2;
        cycle++;
    }
    return hh;
}
int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << height(n) << endl;
    }
}
