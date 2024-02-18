#include <iostream>

using namespace std;
int max1 = 0;
struct Node{
    int val;
    Node* next;
    Node* prev;
    int cnt;
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
    void push(int val){
        Node * NewNode = new Node(val);
        if (head == NULL){
            head = tail = NewNode;
            head -> cnt = 0;
        }
        else{
            tail -> next = NewNode;
            NewNode -> prev = tail;
            tail = NewNode;
            max1++;
            tail -> cnt = max1;
        }
    }
    void insert(int a, int b){
        Node* cur = head;
        Node * NewNode = new Node(a);
        while(cur != NULL){
            if(cur -> cnt == b){
                cur -> cnt = b + 1;
                if(cur -> prev){
                    if(cur -> next){
                        cur -> prev -> next = NewNode;
                        NewNode -> prev = cur -> prev;
                        NewNode -> next = cur;
                        cur -> prev = NewNode;
                        NewNode -> cnt = b;
                    }
                    else{
                        cur -> prev -> next = NewNode;
                        NewNode -> next = cur;
                        NewNode -> cnt = b;
                    }
                }
                else{
                    if(cur -> next){
                        head = NewNode;
                        NewNode -> next = cur;
                        NewNode -> cnt = b;
                    }
                    else{
                        head = NewNode;
                        NewNode -> cnt;
                    }
                }
                break;
            }
            cur = cur -> next;
        }
    }
    void print(){
        Node * cur = head;
        while(cur != NULL){
            cout << cur -> val << " ";
            cur = cur->next;
        }
    }
};

int main(){
    int n;
    cin >> n;
    LinkedList list;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        list.push(x);
    }
    int a,b;
    cin >> a >> b;
    // list.sort();
    if(b == n){
        list.push(a);
    }
    else{
        list.insert(a,b);
    }
    list.print();
}