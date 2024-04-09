#include <iostream>

using namespace std;
int cnt = 0;
struct Heap {
    void heapify(int arr[], int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if(l < n && arr[l] > arr[largest]) largest = l;
        if(r < n && arr[r] > arr[largest]) largest = r;
        if(largest != i) {
            swap(arr[largest], arr[i]);
            heapify(arr, n, largest);
        } 
    }
    void buildHeap(int arr[], int n) {
        int index = n / 2 - 1;
        for(int i = index; i >= 0; i--) {
            heapify(arr, n, i);
        }
    }
    void searchHeap(int arr[], int n) {
        for(int i =0; i < n; i++) {
            int l = 2 * i + 1;
            int r = 2 * i + 2;
            if(l < n && r < n && arr[l] < arr[r]) cnt++;
        }
    }
    void printHeap(int arr[], int n) {
        for(int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
    }

};
int main() {
    int n; cin >> n;
    int arr[n];
    Heap heap;
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    heap.buildHeap(arr, n);
    heap.searchHeap(arr, n);
    cout << cnt;
}
