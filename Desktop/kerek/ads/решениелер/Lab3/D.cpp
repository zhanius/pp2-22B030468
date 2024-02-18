#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int lowerIndex(int arr[], int n, int x) {
    int l = 0, h = n - 1;
    while (l <= h) {
        int mid = (l + h) / 2;
        if (arr[mid] >= x)
            h = mid - 1;
        else
            l = mid + 1;
    }
    return l;
}

int upperIndex(int arr[], int n, int x) {
    int l = 0, h = n - 1;
    while(l <= h) {
        int mid = (l + h) / 2;
        if (arr[mid] <= x)
            l = mid + 1;
        else
            h = mid - 1;
    }
    return h;
}

vector <int> nonOverlap(int l1, int r1, int l2, int r2) {
    // l1 r1 range is always a greater range
    if ((r1 - l1) < (r2 - l2)) {
        int tmp = r1;
        r1 = r2;
        r2 = tmp;
        tmp = l1;
        l1 = l2;
        l2 = tmp;
    }
    if (r2 <= r1 && l2 >= l1 )
        // действие только для одного интервала л1 р1
        return {l1, r1};
    else if (r2 <= r1 && r2 >= l1 && l2 < l1)
        // перемешаем правый конец второго интервала перед началом второго интервала
        r2 = l1 - 1;
    else if (r2 > r1 && l2 < r1)
        // перемещаем левый конец второго интервала после конца второго интервала
        l2 = r1 + 1;
    return{l1, r1, l2, r2};
}

int main() {
    int n, q; cin >> n >> q;
    int v[n];
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    sort(v, v+n);
    while(q--) {
        int l1, r1, l2, r2, res;
        cin >> l1 >> r1 >> l2 >> r2;
        vector <int> newRanges = nonOverlap(l1, r1, l2, r2);
        if (newRanges.size() > 2) {
            res = (upperIndex(v, n, newRanges[1]) - lowerIndex(v, n, newRanges[0]) + 1) + (upperIndex(v, n, newRanges[3]) - lowerIndex(v, n, newRanges[2]) + 1);
        }
        else {
            res = upperIndex(v, n, newRanges[1]) - lowerIndex(v, n, newRanges[0]) + 1;
        }
        cout << res << "\n";
    }
}