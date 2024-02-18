#include <iostream>
#include <math.h>
#include <stack>

using namespace std;

bool isPrime(int n) {
    if (n > 1)
        for(int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }
    else
        return false;
    return true;
}

int main() {
    int n;
    cin >> n;
    stack <int> s;
    int cnt = 0, prime, supercnt = 0;
    for (int i = 2; supercnt < n; i++) {
        if (isPrime(i)) {
            cnt++;
            if (isPrime(cnt)) {
                prime = i;
                s.push(prime);
                supercnt++;
            }
        }
    }
    cout << s.top();
}