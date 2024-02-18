#include <iostream>
#include <cmath>
using namespace std;

int ans = 0;
struct Node{
    int val;
    Node* next;
    Node* prev;
    Node(int val){
        this->val = val;
        this->prev = NULL;
        this->next = NULL;
    }
};

class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(int val){
        Node* newNode = new Node(val);
        if(head == NULL){
            head = tail = newNode;
        }
        else{
            tail->next = newNode;
            newNode->prev=tail;
            tail=newNode;
        }
    }
    void find(int x) {
        Node* cur = head;
        int diff = INT_MAX;
        int cnt = 0;
        while (cur != NULL) {
            if (abs(cur->val - x) < diff) {
                diff = abs(cur->val - x);
                ans = cnt;
            } if (cur -> val == x){
                ans = cnt;
                break;
            }
            cnt++;
            cur = cur -> next;
        }
    }
};

int main(){
    int n; cin >> n;
    LinkedList list;
    while(n--){
        int r; cin >> r;
        list.push(r);
    }
    int x; cin >> x;
    list.find(x);
    cout << ans;
}