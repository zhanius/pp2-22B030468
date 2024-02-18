#include <iostream>
#include <queue>

using namespace std;

int main() {
    queue <int> boris, nursik;
    for (int i = 0; i < 5; i++) {
        int n;
        cin >> n;
        boris.push(n);
    }
    for (int i = 0; i < 5; i++) {
        int n;
        cin >> n;
        nursik.push(n);
    }
    int cnt = 0;
    while(!boris.empty() && !nursik.empty()) {
        if (cnt > 1000000) {
            cout << "blin nichya";
            return 0;
        }
        if (boris.front() == 0 && nursik.front() == 9) {
            boris.push(boris.front());
            boris.push(nursik.front());
            boris.pop();
            nursik.pop();
        }
        else if (boris.front() == 9 && nursik.front() == 0) {
            nursik.push(boris.front());
            nursik.push(nursik.front());
            boris.pop();
            nursik.pop();
        }
        else if (boris.front() > nursik.front()) {
            boris.push(boris.front());
            boris.push(nursik.front());
            boris.pop();
            nursik.pop();
        }
        else if (boris.front() < nursik.front()){
            nursik.push(boris.front());
            nursik.push(nursik.front());
            boris.pop();
            nursik.pop();
        }
        cnt++;
    }
    if(boris.empty())
        cout << "Nursik " << cnt;
    else
        cout << "Boris " << cnt;
}