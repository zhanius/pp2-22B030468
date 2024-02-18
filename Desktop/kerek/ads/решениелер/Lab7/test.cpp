#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
bool comparator(int a[], int b[]){
   if(a[2] == b[2]){
        if(a[1] == b[1]){
            return a[0] < b[0];
        }
        return a[1] < b[1];
   }
    return a[2] < b[2];
}

int partition(int a[][3], int low, int high){
    int pivot = high;
    int i = low - 1;
    for(int j = low; j <= high-1; j++){
        if(comparator(a[j], a[pivot])){
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i+1], a[high]);
    return i + 1;
}

void quickSort(int a[][3], int low, int high){
    if(low < high){
        int pi = partition(a, low, high);
        quickSort(a, low, pi-1);
        quickSort(a, pi+1, high);
    }
}

int main(){
    int n;cin >> n;
    int a[n][3];
    for(int i = 0; i < n;i++){
        string s;cin >> s;
        string s1 = s.substr(0,2);
        string s2 = s.substr(3,2);
        string s3 = s.substr(6,4);
        int x1 = stoi(s1);
        int x2 = stoi(s2);
        int x3 = stoi(s3);
        a[i][0] = x1;
        a[i][1] = x2;
        a[i][2] = x3;
    }
    quickSort(a, 0, n-1);
    // for(int i = n-1; i >= 0; i--){
    //     if(a[i][0] < 10) cout << 0;
    //     cout << a[i][0] << "-";
    //     if(a[i][1] < 10) cout << 0;
    //     cout << a[i][1] << "-";
    //     cout << a[i][2] << '\n';
    //     // cout << a[i][0] << "-" << a[i][1] << "-" << a[i][2] << '\n';
    // }
    for(int i = 0; i < n; i++){
        cout << a[i][0] << "-" << a[i][1] << "-" << a[i][2] << '\n';
    }

}