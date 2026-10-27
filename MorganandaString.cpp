#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'morganAndString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 */
vector<int> suffixArray(string text)
{
    int nt = text.size();
    int mm = 62;
    vector<int> cntr(mm, 0);
    for(int i = 0; i< nt; i++){
        int r = text[i] - 'A';
        cntr[r] += 1;
    }
    for(int i = 1; i < mm; i++){
        cntr[i] += cntr[i-1];
    }
    vector<int> p(nt, -1);
    for(int i=0; i < nt; i++){
        int a = text[i] - 'A';
        p[cntr[a]-1] = i;
        cntr[a] -= 1;
    }
    //print(p)
    vector<int> c(nt, -1);
    c[p[0]] = 0; // class index by suffix
    for(int i = 1; i < nt; i++){
        if(text[p[i]] > text[p[i-1]]){
            c[p[i]] = c[p[i-1]]+1;
        }else{
            c[p[i]] = c[p[i-1]];
        }
    } 
    //print(c)
    int k = 1;
    vector<int> pn(nt, -1);
    vector<int> cn(nt, -1);
    while(k < nt){
        for(int i = 0; i < nt; i++){
            pn[i] = p[i] - k >= 0 ? p[i] - k:p[i] - k + nt;
        }
        int cls = c[p[nt-1]]+1;
        //print(cls)
        //print(pn)
        vector<int> cntr2(cls, 0);
        for(int i = 0; i < nt; i++)
            cntr2[c[i]] += 1;
        for(int i = 1; i < cls; i++)
            cntr2[i] += cntr2[i-1];
        for(int i = nt-1; i > -1; i--){
            int a = pn[i];
            int b = cntr2[c[a]]-1;
            p[b] = a;
            cntr2[c[a]] -= 1;
        }
        //print(p)
        cn[p[0]] = 0;
        for(int i = 1; i < nt; i++){
            int a = p[i];
            int ak = (a+k)%nt;
            int b = p[i-1];
            int bk = (b+k)%nt;
            if(c[a] == c[b] && c[ak] == c[bk]){
                cn[a] = cn[b];
            }else{
                cn[a] = cn[b]+1;
            }
        }
        for(int i = 0; i < nt; i++)
            c[i] = cn[i];    
        k *= 2;
    }
    vector<int> rank(nt, -1);
    for(int i = 0; i < nt; i++)
        rank[p[i]] = i;
    return rank;
}

string morganAndString(string a, string b) {
    string text = a+'a'+b+'a';
    vector<int> sarr = suffixArray(text);
    //cout<<'a'-'A'<<endl;
    int na = a.size();
    int nb = b.size();
    int i = 0;
    int j = 0;
    string c;
    while(i < na or j < nb){
        if (sarr[i] < sarr[na+1+j]){
            c += a[i];
            i += 1;
        }else{
            c += b[j];
            j += 1;
        }
    }
    return c;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string a;
        getline(cin, a);

        string b;
        getline(cin, b);

        string result = morganAndString(a, b);

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
