#include <iostream>
#include <algorithm>

using namespace std;

struct Heap {
    int *a;
    int capacity;
    int size;

    int parent (int i) {
        return (i-1)/2;
    }
    int left (int i) {
        return i*2 + 1;
    }
    int right (int i) {
        return i*2 + 2;
    }
    void heapUp (int i) {
        int p = parent(i);
        if (a[i] > a[p]) {
            swap(a[i], a[p]);
            heapUp(p);
        }
    }
    void heapDown (int i) {
        int l = left(i);
        int r = right(i);
        int max = i;
        if (i < size && a[max] < a[l]) {
            max = l;
        }
        if (i < size && a[max] < a[r]) {
            max = r;
        }
        if (max != i) {
            swap(a[max], a[i]);
            heapDown(max);
        }
    }
    void add (int x) {
        a[size] = x;
        size++;
        heapUp(size-1);
    }

    void cut_max () {
        a[0] = a[size-1];
        size = max(0, size - 1);
        heapDown(0);
    }
    
    Heap (int x) {
        this->a = new int[x];
        this->size = 0;
        this->capacity = x;
    }
};

int main() {

}