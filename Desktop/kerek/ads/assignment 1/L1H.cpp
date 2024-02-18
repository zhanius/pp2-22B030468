#include <iostream>
#include <queue>
#include <math.h>

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
    queue <bool> useless;
    cin >> n;
    if (isPrime(n)) {
        useless.push(true);
    }
    else 
        useless.push(false);
    cout << ((useless.front()) ? "YES" : "NO");
}