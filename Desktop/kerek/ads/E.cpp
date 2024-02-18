#include <iostream>

using namespace std;
int count = 0;
struct Node{
    string val;
    int cnt;
    int cnt2;
    Node* next;
    Node* prev;
    Node(string val){
        this -> val = val;
        next = NULL;
        prev = NULL;
        cnt = 1;
        cnt2 = 0;
    }
};

class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(string val){
        Node* NewNode = new Node(val);
        if(head == NULL){
            head = tail = NewNode;
            count++;
        }
        else{
            if(tail -> val == val){
                tail -> cnt++;
            }
            else{
                if(NewNode -> cnt > 1){
                    NewNode -> cnt2++;
                    count--;
                }
                else{
                    tail -> next = NewNode;
                    NewNode -> prev = tail;
                    tail = NewNode;
                    count++;
                }
            }
        }
    }
    void sort(){
        Node *i = head;
        Node *j = head -> next;
        while(i -> next != NULL){
            while(j != NULL){
                if (i -> val < j -> val){
                    swap(i -> val, j -> val);
                    swap(i -> cnt, j -> cnt);
                }
                j = j -> next;
            }
            i = i -> next;
            j = i;
        }
    }
    void print(){
        Node * cur = tail;
        while(cur != NULL){
            if(cur -> cnt2 == 0){
                cout << cur -> val << endl;
            }
            cur = cur->prev;
        }
    }
};

int main(){
    int n;
    cin >> n;
    LinkedList list;
    while(n--){
        string x;
        cin >> x;
        if(x != "" && x != " "){
            list.push(x);
        }
    }
    // list.sort();
    cout << "All in all: " << count << endl << "Students:" << endl;
    list.print();
}