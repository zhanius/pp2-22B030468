#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    queue <char> q;
    map <char, int> m;
    int kcnt = 0, scnt = 0;
    cin >> s;
    for(int i = 0; i < s.length(); i++) {
        q.push(s[i]);
        m[s[i]]++;
    }
    while(m['K'] > 0 && m['S'] > 0) {
        if (q.front() == 'S' && scnt == 0) {
            if (m['K'] > 0) {
                kcnt++;
                m['K']--;
            }
            q.push(q.front());
            q.pop();
        }
        else if (q.front() == 'S' && scnt > 0) {
            q.pop();
            scnt--;
        }
        else if (q.front() == 'K' && kcnt == 0){
            if (m['S'] > 0) {
                scnt++;
                m['S']--;
            }
            q.push(q.front());
            q.pop();
        }
        else if (q.front() == 'K' && kcnt > 0) {
            q.pop();
            kcnt--;
        }
    }
    if (m['K'] > 0)
        cout << "KATSURAGI";
    else
        cout << "SAKAYANAGI";
}