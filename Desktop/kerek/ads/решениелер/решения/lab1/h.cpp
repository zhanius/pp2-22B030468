#include <iostream>
#include <deque>
using namespace std;

int main() {
    int n;
    cin >> n;

    deque<int> dq;
    char operation;
    int num;

    while (n--) {
        cin >> operation;
        if (operation == '!') {
            if (dq.empty()) {
                cout << "No elements to sum!" << endl;
            } else {
                int sum = dq.front() + dq.back();
                cout << sum << endl;
            }
        } else if (operation == '+') {
            cin >> num;
            dq.push_front(num);
        } else if (operation == '-') {
            cin >> num;
            dq.push_back(num);
        } else if (operation == '*') {
            if (!dq.empty()) {
                int sum = dq.front() + dq.back();
                cout << sum << endl;
                dq.pop_front();
                dq.pop_back();
            } else {
                cout << "No elements to sum!" << endl;
            }
        }
    }

    return 0;
}