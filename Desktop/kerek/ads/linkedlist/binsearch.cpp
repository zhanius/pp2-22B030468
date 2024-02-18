#include <iostream>
using namespace std;

int a[100005];
bool lin_search(int a[], int x, int n){
    for(int i = 1; i<=n; i++ )
        if(a[i] == x) return true;
    return false;
}

bool bin_search(int a[], int x, int l, int r){
    sort(a,a+r);
    while(l <= r){
        int mid = l + (r-l)/2;
        if(a[mid]==x){
            return true;
        }
        if(a[mid]<x){
            l = mid + 1;
        }
        else{
            r = mid - 1;
        }
    }
    return false;
}


int main(){
    int n; cin >> n;
    int x;
    int a[n];
    for(int i = 1; i <= n; i++){
        cin >> x;
    }
    bool lin = lin_search(a, x, n);
    bool bin = bin_search(a, x, 0, n - 1);
    cout << lin ? "yup":"nope" << endl;
    cout << bin ? "yup":"nope" << endl;
}

