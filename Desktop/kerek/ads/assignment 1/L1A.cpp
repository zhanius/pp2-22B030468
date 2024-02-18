#include <iostream>
#include <deque>
 using namespace std;

 int main() {
     int n; cin >> n;
     int a;
     deque <int> d;
     while(n--) {
        cin >> a;
        int b = a;
        d.push_front(b--);
        while (b > 0) {
            d.push_front(b);
            for(int j = 0; j < b; j++) {
                d.push_front(d.back());
                d.pop_back();
            }
            b--;
        }
        while(!d.empty()) {
            cout << d.front() << " ";
            d.pop_front();
        }
        cout << "\n";
     }
 }