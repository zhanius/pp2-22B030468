#include <iostream>
#include <math.h>

using namespace std;

struct node {
  int value;
  node* next;

  node() {
      this->value = 0;
      this->next = NULL;
  }
  node(int data) {
      this->value = data;
      this->next = NULL;
  }
  node(int data, node* next) {
      this->value = data;
      this->next = next;
  }
};

node *reverse(node *head) {
    node *cur = head;
    node *next;
    node *prev = NULL;
    while (next != NULL) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    head = prev;
    return head;
}
 
int main() {
    node *head;
    node *cur;
    int n, cnt = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        if (i == 0) {
            head = new node(a);
            cur = head;
        }
        else {
            cur->next = new node(a);
            cur = cur->next;
        }
    }
    // int target, diff = INT32_MAX, min;
    // cur = head;
    // cin >> target;
    // while(cur != NULL) {
    //     if(abs(cur->value - target) < diff) {
    //         diff = abs(cur->value - target);
    //         min = cnt;
    //     }
    //     cnt++;
    //     cur = cur->next;
    // }
    // cout << min;
    
    head = reverse(head);
    cur = head;
    while(cur != NULL) {
        cout << cur->value << " ";
        cur = cur->next;
    }
}