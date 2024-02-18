#include <iostream>
#include <set>

using namespace std;

int g[500][500];
int added[500];
int ans[500];
bool used[500];
bool work[500];
int dist = 0;

void floydWarshall(int n) {
    int i, j, k;
    for (k = 0; k < n; k++) {
        int across = added[k];
        used[across] = true;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                g[i][j] = min(g[i][j], g[i][across] + g[across][j]);
                
            }
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