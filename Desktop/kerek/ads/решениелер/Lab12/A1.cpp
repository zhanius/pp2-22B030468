#include <iostream>

using namespace std;

int g[500][500];
int added[500];
int ans[500];

void floydWarshall(int n) {
    int i, j, k;
    for (k = 0; k < n; k++) {
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
            cout << ans[k] << ' ';
        }
        
    }
    cout << '\n';
}

int main() {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> g[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        cin >> added[i];
        added[i]--;
    }
    floydWarshall(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << g[i][j] << ' ';
        }
        cout << '\n';
    }
    for (int i = 0; i < n; i++) {
        cout << ans[i] << ' ';
    }
}