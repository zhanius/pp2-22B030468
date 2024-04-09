#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector <vector <int> > g (10000, vector <int> (10000, 0));
    g[9999][9999] = 1;
    cout << g[9999][9999];
}