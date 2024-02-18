#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

const int INF = 1000000000;
vector <pair <int, int> > g[200005];
vector <int> d(200005, INF);
int n, m;

// function of dijkstra
int shortest_path (int s, int dest) {
    d.clear();
    for (int i = 0; i < n; i++) {
        d[i] = INF;
    }
    d[s] = 0;
    set <pair <int, int> > q;
    q.insert(make_pair(0, s));
    while(!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());
        for (int j = 0; j < g[v].size(); j++) {
            int to = g[v][j].first, len = g[v][j].second;
            if (d[v] + len < d[to]) {
                q.erase(make_pair(d[to], to));
                d[to] = d[v] + len;
                q.insert(make_pair(d[to], to));
            }
        }
    }
    return d[dest];
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});
        g[b].push_back({a, c});
    }
    int s, a, b, f; cin >> s >> a >> b >> f;
    int first, second;
    first = shortest_path(s, a) + shortest_path(a, b) + shortest_path(b, f);
    second = shortest_path(s, b) + shortest_path(b, a) + shortest_path(a, f);
    if(min(first, second) <= INF){ 
        cout << min(first, second); 
    }else{ 
        cout << -1; 
    } 
}