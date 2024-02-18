#include <iostream>
using namespace std;

struct Node{
    string val;
    Node* next;
    Node* prev;
    Node(string val){
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(string val){
        Node* newNode = new Node(val);
        if(head == NULL){
            head = tail = newNode;
        }
        else{
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }
    void show(int x){
        while(x--){
            this->push(head->val);
            head = head -> next;
        }
        while(head){
            cout << head->val << ' ';
            head = head->next;
        }
    }
};
int main(){
    int n, k; cin >> n >> k;
    LinkedList list;
    while(n--){
        string s; cin >> s;
        list.push(s);
    }
    list.show(k);
}
