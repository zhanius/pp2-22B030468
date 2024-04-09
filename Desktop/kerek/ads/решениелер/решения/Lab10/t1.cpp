#include <iostream>
#include <vector>

using namespace std;
const int INF = 100000000;
const int N = 2 * 1e5 + 1;
int g[N][N];
int main(){
 long long n,m,l,r,w;
 cin >> n >> m;
 int g[n][n];
 vector<bool> used(n);
 vector<int> min_e(n, INF), sel_e(n, -1);
 for(int i = 0; i < m; i++){
  cin >> l >> r >> w;
  for(int j = l; j <= r; j++){
   for(int k = j+1; k<=r; k++){
    g[j][k] = w;
    // g[k][j] = w;
   }
  }
 }
 for(int i = 1; i <= n; i++){
  for(int j = 1; j <= n; j++){
   cout << g[i][j] << " ";
  }
  cout << endl;
 }
 // min_e[0] = 0;
 // for(int i = 0; i < n; ++i){
 //  int v = -1;
 //  for(int j = 0; j < n; ++j){
 //   if(!used[j] and (v == -1 or min_e[j] < min_e[v]))
 //    v = j;
 //  }
 //  if(min_e[v] == INF){
 //   cout << "NO MST!";
 //   return 0;
 //  }
 //  used[v] = true;
 //  if(sel_e[v] != -1){
 //   cout << v << " " << sel_e[v] << endl;
 //  }
 //  for(int to = 0; to < n; ++to)
 //   if(g[v][to] < min_e[to]){
 //    min_e[to] = g[v][to];
 //    sel_e[to] = v;
 //   }



 }