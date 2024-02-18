#include <iostream>
#include <deque>

using namespace std;

int main() {
    deque <int> d;
    while(1) {
        char c;
        cin >> c;
        if (c == '!')
            break;
        if (c == '+') {
            int n;
            cin >> n;
            d.push_front(n);
        }
        if (c == '-') {
            int n;
            cin >> n;
            d.push_back(n);
        }
        if (c == '*') {
            if (d.size() < 1) {
                cout << "error\n";
            }
            else if (d.size() >= 2 ){
                cout << d.front() + d.back() << '\n'; // 
                d.pop_front();
                d.pop_back();
            }
            else if (d.size() == 1) {
                cout << d.front() * 2 << '\n';
                d.pop_front();
            }
        }
        
    }
}