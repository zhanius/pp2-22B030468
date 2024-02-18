#include <iostream>
using namespace std;

struct node{
    int val;
    node* next;
    node* prev;
    node(int val){
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

class LinkedList{
public:
    node* head = NULL;
    node* tail = NULL;
    void push(int val){
        node* nw = new node(val);
        if(head == NULL){
            head = tail = nw;
        }
        else{
            head -> next = nw;
            nw -> prev = tail;
            tail = nw;
        }
    }

    void print(){
        while(head){
            cout << head -> val << ' ';
            head = head -> next;
        }
    }
};

int main(){
    LinkedList l;
    l.push(5);
    l.push(7);
    l.print();
}
#include <iostream>
using namespace std;

struct Node{
    int val;
    Node* next;
    Node* prev;
    Node(int val){
        this->val=val;
        this->next=NULL;
        this->prev=NULL;
    }
};

class LinkedList{
public:
    Node* head=NULL;
    Node* tail=NULL;
    void add(int val){
        Node* nw=new Node(val);
        if(head==NULL){
            head=tail=nw;
        }
        else{
            tail->next=nw;
            nw->prev=tail;
            tail=nw;
        }
    }
    void show(){
        int cnt=0;
        while(head){
            (cnt%2==1)?cout<<" ":cout<<head->val;
            head=head->next;
            cnt++;
        }
    }
};

int main(){
    int n;cin>>n;
    LinkedList list;
    while(n--){
        int x;cin>>x;
        list.add(x);
    }
    list.show();
}