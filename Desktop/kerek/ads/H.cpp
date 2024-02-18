#include <iostream>
#include <stack>
using namespace std;
int count = 0;
struct Node{
    int val;
    Node* next;
    Node* prev;
    Node(int val){
        this -> val = val;
        next = NULL;
        prev = NULL;
    }
};

class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(int val,int pos){
        Node* NewNode = new Node(val);
        int cnt = 0;
        if(head == NULL){
            head = tail = NewNode;
            count++;
            return;
        }
        else if(pos == count){
            tail -> next = NewNode;
            NewNode -> prev = tail;
            tail = NewNode;
            count++;
            return;
        }
        else if(pos == 0){
            NewNode -> next = head;
            head -> prev = NewNode;
            head = NewNode;
            count++;
            return;
        }
        Node* cur = head;
        while(cnt != pos){
            cur = cur -> next;
            cnt++;
        }
        NewNode -> prev = cur -> prev;
        NewNode -> next = cur;
        cur -> prev = NewNode;
        cur -> prev -> prev -> next = NewNode;
        count++;
    }
    void Remove(int pos){
        int cnt = 0;
        if(pos == 0){
            head = head -> next;
            head -> prev = NULL;
            count--;
            return;
        }
        Node* cur = head;
        if(pos == count - 1){
            tail -> prev -> next = NULL;
            tail = tail -> prev;
            count--;
            return;
        }
        while(cnt != pos){
            cur = cur -> next;
            cnt++;
        }
        cur -> next -> prev = cur -> prev;
        cur -> prev -> next = cur -> next;
        cur = NULL;
        count--;
    }
    void swap(int pos1, int pos2){
        Node* cur = head;
        int cnt = 0;
        while(cnt != pos1){
            cur = cur -> next;
            cnt++;
        }
        int c = cur -> val;
        Remove(pos1);
        push(c,pos2);
    }
    void reverse(){
        Node* cur = head;
        Node* next = NULL;
        Node* prev = NULL;
        tail = cur;
        while(cur){
            next = cur -> next;
            cur -> prev = next;
            cur -> next = prev;
            prev = cur;
            cur = next;
        }
        head = prev;
    }
    void cyclic_shift_left(int k){
        int cnt=0;
        Node* cur = head;
        while(cur){
            if(cnt == k%count){
                head = cur;
                return;
            }
            else{
                Node* newNode = new Node(cur->val);
                tail -> next = newNode;
                newNode -> prev = tail;
                tail = tail -> next;
                head = head -> next;
                head -> prev = NULL;
            }
            cur = cur -> next;
            cnt++;
        }
    }
    void cyclic_shift_right(int k){
        int cnt = 0;
        Node* cur = tail;
        while(cur){
            if(cnt == k % count){
                tail = cur;
                return;
            }
            else{
                Node * newNode = new Node(cur -> val);
                head -> prev = newNode;
                newNode -> next = head;
                head = newNode;
                tail = tail -> prev;
                tail -> next = NULL;
            }
            cur = cur -> prev;
            cnt++;
        }
    }
    void print(){
        Node * cur = head;
        if(cur == NULL){
            cout << -1 << endl;
            return;
        }
        while(cur != NULL){
            cout << cur -> val << " ";
            cur = cur -> next;
        }
        cout << endl;
    }
};

int main(){
    LinkedList list;
    char n;
    bool ok = true;
    while(ok){
        cin >> n;
        if(n == '0'){
            ok = false;
        }
        if(n == '1'){
            int a,b;
            cin >> a >> b;
            list.push(a,b);
        }
        if(n == '2'){
            int a;
            cin >> a;
            list.Remove(a);
        }
        if(n == '3'){
            list.print();
        }
        if(n == '4'){
            int a,b;
            cin >> a >> b;
            if(a != b){
                list.swap(a,b);
            }
        }
        if(n == '5'){
            list.reverse();
        }
        if(n == '6'){
            int a;
            cin >> a;
            list.cyclic_shift_left(a);
        }
        if(n == '7'){
            int a;
            cin >> a;
            list.cyclic_shift_right(a);
        }
    }
}