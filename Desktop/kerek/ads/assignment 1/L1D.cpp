#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s;
    stack <char> st;
    cin >> s;
    for (int i = 0; i < s.length(); i++) {
        if (!st.empty() && st.top() == s[i]) {
           st.pop();
        }
        else
            st.push(s[i]);
    }
    if (st.empty())
        cout << "YES";
    else
        cout << "NO";
}