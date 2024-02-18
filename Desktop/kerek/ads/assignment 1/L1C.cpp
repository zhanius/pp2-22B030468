#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    stack <char> st;
    for(int i = 0; i < s1.length(); i++) {
        if(s1[i] == '#')
            st.pop();
        else
            st.push(s1[i]);
    }
    for(int i = s2.length() - 1; i >= 0; i--) {
        if(s2[i] == '#') {
            i--;
            continue;
        }
        else
            if (s2[i] == st.top()) {
                st.pop();
            }
            else
                {
                    cout << "No";
                    return 0;
                }
    }
    if (st.empty())
        cout << "Yes";
    else
        cout << "No";
}