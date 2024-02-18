#include <iostream>

using namespace std;

struct Node{
    int val;
    Node* prev;
    Node* next;
    Node(int val){
        this -> val = val;
        prev = NULL;
        next = NULL;
    }
};
class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(int val){
        Node* NewNode = new Node(val);
        if(head == NULL){
            head = tail = NewNode;
        }
        else{
            tail -> next = NewNode;
            NewNode -> prev = tail;
            tail = NewNode;
        }
    }
    void max_sum(){
        Node* i = head;
        Node* j = head;
        int sum = 0;
        int max = -10000000;
        while(i -> next != NULL){
            while(j != NULL){
                sum += j -> val;
                // cout << j -> val << endl;
                if(sum > max){
                    max = sum;
                }
                j = j -> next;
            }
            i = i -> next;
            j = i;
            sum = 0;
        }
        cout << max;
    }
    void print(){
        Node* cur = head;
        while(cur != NULL){
            cout << cur -> val << " ";
            cur = cur -> next;
        }
    }
};


int main(){
    int n;
    cin >> n;
    LinkedList list;
    while(n--){
        int x;
        cin >> x;
        list.push(x);
    }
    list.max_sum();
    // list.print();
}