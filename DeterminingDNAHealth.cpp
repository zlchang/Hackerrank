#include <bits/stdc++.h>
#include <stack>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

int nletters = 26;
int mnodes = 100001;
int mgenes = 2000001;
vector<vector<int>> trie(mgenes, vector<int>(nletters, -1));
vector<int> fail(mgenes, -1);
vector<vector<int>> tree(mgenes);
vector<int> hstart(mgenes, 0);
vector<int> hend(mgenes, 0);
vector<int> gnodes(mnodes);
vector<vector<int>> snodes(mnodes);

int node = 0;
void build_strand(vector<string> gs){
    int n = gs.size();
    
    for(int i = 0; i < n; i++){
        int current = 0;
        for(char l : gs[i]){
            int j = l - 'a';
            if (trie[current][j] == -1){
                trie[current][j] = node+1;
                //cout<<current<<" "<<l<<" " <<node+1<<endl;
                node += 1;
            }
            current = trie[current][j];
            snodes[i].push_back(current);
        }
        //cout<<i<<" "<<current<<endl;
    }
}
void build(vector<string> gs){
    int n = gs.size();
    vector<int> output(n);
    for(int i = 0; i < n; i++){
        int current = 0;
        for(char l : gs[i]){
            int j = l - 'a';
            if (trie[current][j] == -1){
                trie[current][j] = node+1;
                //cout<<current<<" "<<l<<" " <<node+1<<endl;
                node += 1;
            }
            current = trie[current][j];
        }
        gnodes[i] = current;
        //cout<<i<<" "<<current<<endl;
    }
}
void suffix(){
    fail[0] = 0;
    queue<int> qq;
    qq.push(0);
    while(qq.size() > 0){
        int state = qq.front();
        qq.pop();
        for (int i = 0; i < nletters; i++){
            if (trie[state][i] != -1){
                int suffix = fail[state];
                int child = trie[state][i];
                if (state == 0)
                    fail[child] = 0;
                else{
                    while(trie[suffix][i] == -1 and suffix > 0)
                        suffix = fail[suffix];
                    if(trie[suffix][i] != -1)
                        fail[child] = trie[suffix][i];
                    else
                        fail[child] = 0;
                }
                int fchild = fail[child];
                tree[fchild].push_back(child);
                //cout<<fchild<<" "<<child<<endl;
                qq.push(child);
            }
        }
    }
}
void dfs(int parent)
{
    hstart[parent] = node;
    node += 1;
    for(int child: tree[parent]){
        dfs(child);
    }
    hend[parent] = node;  
}
void get_index(){
    stack<int> stk;
    stack<int> visited;
    stk.push(0);
    node = 0;
    while(!stk.empty()){
        int state = stk.top();
        //cout<<state<<endl;
        if(visited.empty() != 1 && visited.top() == state){
            hend[state] = node;
            //cout<<"pop "<<state<<endl;
            //cout<<"end: "<<state<<" "<<node<<endl;
            stk.pop();
            visited.pop();
        }else{
            visited.push(state);
            hstart[state] = node;
            //cout<<state<<" "<<node<<endl;
            node += 1;
            for(int child: tree[state]){
                stk.push(child);
            }
        }
    }
}
vector<long long> fenwick(mgenes, 0);
void update(int a, int value){
    while(a < node){
        fenwick[a] += value;
        a += a & (-a);
    }
}
long long query(int a){
    long long sum = 0;
    while(a > 0){
        sum += fenwick[a];
        a -= a& (-a);
    }
    return sum;
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string genes_temp_temp;
    getline(cin, genes_temp_temp);

    vector<string> genes_temp = split(rtrim(genes_temp_temp));

    vector<string> genes(n);

    for (int i = 0; i < n; i++) {
        string genes_item = genes_temp[i];
        genes[i] = genes_item;
    }
 
    string health_temp_temp;
    getline(cin, health_temp_temp);

    vector<string> health_temp = split(rtrim(health_temp_temp));

    vector<int> health(n);

    for (int i = 0; i < n; i++) {
        int health_item = stoi(health_temp[i]);

        health[i] = health_item;
    }
    
    
    string s_temp;
    getline(cin, s_temp);

    int s = stoi(ltrim(rtrim(s_temp)));
    
    vector<string> strands(s);
    vector<vector<int>> sfirst(n);
    vector<vector<int>> slast(n);
    for (int s_itr = 0; s_itr < s; s_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int first = stoi(first_multiple_input[0]);

        int last = stoi(first_multiple_input[1]);

        string d = first_multiple_input[2];
        strands[s_itr] = d;
        if (first > 0){
            sfirst[first-1].push_back(s_itr);
        }
        slast[last].push_back(s_itr);  
    }
    build(genes);
    build_strand(strands);
    suffix();
    get_index();
    //cout<<"node "<<node<<endl;
    //node = 0;
    //dfs(0);
    vector<long long> results(s, 0);
 
    for(int i = 0; i < n; i++){
        int gnode = gnodes[i];
        int val = health[i];
        //cout<<gnode<<" val: "<<val<<endl;
        update(hstart[gnode], val);
        //cout<<"query start: "<<query(hstart[gnode])<<endl;
        update(hend[gnode], -val);
        //cout<<"query end: "<<query(hend[gnode])<<endl;
        for(int j: sfirst[i]){
            for(int sj:snodes[j]){
                long long qs = query(hstart[sj]);
                results[j] -= qs;
            }
        }
        for(int j: slast[i]){
            for(int sj:snodes[j]){
                long long qs = query(hstart[sj]);
                results[j] += qs;
            }
        }
    } 
    long long a = -1;
    long long b = -1;
    for(long long res: results){
        if(a == -1){
            a = res;
        }else{
            a = a < res ? a : res;
        }
        if(b == -1){
            b = res;
        }else{
            b = b < res ? res : b;
        }
    }
    cout << a << " " << b << endl;

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
