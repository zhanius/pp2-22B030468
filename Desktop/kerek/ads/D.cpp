#include <iostream>
using namespace std;
int max1 = 1;
struct Node{
    int val;
    int cnt;
    Node* next;
    Node* prev;
    Node(int val){
        this -> val = val;
        next = NULL;
        prev = NULL;
        cnt = 1;
    }
};

class LinkedList{
public:
    Node* head = NULL;
    Node* tail = NULL;
    void push(int val){
        Node * NewNode = new Node(val);
        if (head == NULL){
            head = NewNode;
        }
        else{
            Node * cur = head;
            while(cur != NULL){
                if(cur -> val == val){
                    cur -> cnt++;
                    if(cur -> cnt > max1){
                        max1 = cur -> cnt;
                    }
                    break;
                }
                if(cur -> next == NULL){
                    cur -> next = NewNode;
                    break;
                }
                cur = cur->next;
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
        Node * cur = head;
        while(cur != NULL){
            if(cur -> cnt == max1){
                cout << cur -> val << " ";
            }
            cur = cur->next;
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
    list.sort();
    list.print();
}