#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'squareBoard' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts 2D_INTEGER_ARRAY board as parameter.
 */
const int m = 30;
int primes[] = {0, 0, 1, 1, 0, 1, 0, 1, 0, 0};
int cntr[m+1][m+1] = {0};
int memo[m][m][m][m];
int grundy(int rmin, int rmax, int cmin, int cmax)
{
    if(memo[rmin][rmax-1][cmin][cmax-1] != -1)
        return memo[rmin][rmax-1][cmin][cmax-1];
    int nr = rmax - rmin;
    int nc = cmax - cmin;
    if(nr == 1 && nc == 1){
        memo[rmin][rmax-1][cmin][cmax-1] = 0;
        return 0;
    }
    int cc = cntr[rmax][cmax] - cntr[rmin][cmax] - cntr[rmax][cmin] + cntr[rmin][cmin];

    if(cc == 0){
        memo[rmin][rmax-1][cmin][cmax-1] = 0;
        return 0;
    }

    set<int> gn;
    for(int i = rmin; i < rmax-1; i++){
        int ga = grundy(rmin, i+1, cmin, cmax);
        int gb = grundy(i+1, rmax, cmin, cmax);
        gn.insert(ga^gb);
    }
    for(int i = cmin; i < cmax-1; i++){
        int ga = grundy(rmin, rmax, cmin, i+1);
        int gb = grundy(rmin, rmax, i+1, cmax);
        gn.insert(ga^gb);
    }    
    int i = 0;
    while(gn.find(i) != gn.end()){
        i++;
    }
    memo[rmin][rmax-1][cmin][cmax-1] = i;
    return i;
}

string squareBoard(int n) {
    for(int ia = 0; ia < n; ia++){
        for (int ib = 0; ib < n; ib++){
            for (int ja = 0; ja < n; ja++){
                for (int jb = 0; jb < n; jb++){
                    memo[ia][ib][ja][jb] = -1;
                }
            }
        }
    }
    for(int i = 0; i <n+1; i++){
        cntr[0][i] = 0;
        cntr[i][0] = 0;
    }
    for(int i = 1; i < n+1; i++)
        for(int j = 0; j < n+1; j++)
            cntr[i][j] += cntr[i-1][j];
    for(int i = 0; i < n+1; i++)
        for(int j = 1; j < n+1; j++)
            cntr[i][j] += cntr[i][j-1];
    int res = grundy(0, n, 0, n);

    if (res == 0)
        return string("Second");
    return string("First");
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        for (int i = 0; i < n; i++) {

            string board_row_temp_temp;
            getline(cin, board_row_temp_temp);

            vector<string> board_row_temp = split(rtrim(board_row_temp_temp));

            for (int j = 0; j < n; j++) {
                int board_row_item = stoi(board_row_temp[j]);
                cntr[i+1][j+1] = (primes[board_row_item] == 0);
            }
        }

        string result = squareBoard(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
