#include <iostream>
#include <math.h>
#include <stack>

using namespace std;

bool isPrime(int n) {
    for(int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    stack <int> s;
    int cnt = 0, prime;
    for (int i = 2; cnt < n; i++) {
        if (isPrime(i)) {
            prime = i;
            s.push(prime);
            cnt++;
        }
    }
    cout << s.top();
}