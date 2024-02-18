#include <iostream>

using namespace std;
int cnt = 0;
struct Node{
    string val;
    Node* next;
    Node* prev;
    Node(string n){
        val = n;
        next = NULL;
        prev = NULL;
    }
};
class LinkedList{
public:
    Node* head;
    Node* tail;
    LinkedList(){
        head = NULL;
    }
    void push_front(string n){
        Node* NewNode = new Node(n);
        if(head == NULL){
            head = tail = NewNode;
            cnt++;
        }
        else{
            head -> prev = NewNode;
            NewNode -> next = head;
            head = NewNode;
            cnt++;
        }
        cout << "ok" << endl;
    }
    void push_back(string n){
        Node* NewNode = new Node(n);
        if(head == NULL){
            head = tail = NewNode;
            cnt++;
        }
        else{
            tail -> next = NewNode;
            NewNode -> prev = tail;
            tail = NewNode;
            cnt++;
        }
        cout << "ok" << endl;
    }
    void pop_back(){
        cout << tail -> val << endl;
        if(tail -> prev == NULL){
            tail = head = NULL;
        }
        else{
            tail -> prev -> next = NULL;
            tail = tail -> prev;
        }
        cnt--;
    }
    void pop_front(){
        cout << head -> val << endl;
        if(head -> next == NULL){
            tail = head = NULL;
        }
        else{
            head -> next -> prev = NULL;
            head = head -> next;
        }
        cnt--;
    }
    void size(){
        cout << cnt << endl;
    }
    void front(){
        cout << head -> val << endl;
    }
    void back(){
        cout << tail -> val << endl;
    }
    void clear(){
        Node* cur;
        while(head != NULL){
            cur = head;
            head = head -> next;
        }
        cnt = 0;
        cout << "ok" << endl;
    }
};

int main(){
    LinkedList list;
    string s;
    while(s != "exit"){
        cin >> s;
        string n;
        if(s == "add_front"){
            cin >> n;
            list.push_front(n);
        }
        if(s == "add_back"){
            cin >> n;
            list.push_back(n);
        }
        if(s == "erase_back"){
            if(cnt == 0){
                cout << "error" << endl;
            }
            else{
                list.pop_back();
            }
        }
        if(s == "erase_front"){
            if(cnt == 0){
                cout << "error" << endl;
            }
            else{
                list.pop_front();
            }
        }
        if(s == "front"){
            if(cnt == 0){
                cout << "error" << endl;
            }
            else{
                list.front();
            }
        }
        if(s == "back"){
            if(cnt == 0){
                cout << "error" << endl;
            }
            else{
                list.back();
            }
        }
        if(s == "size"){
            list.size();
        }
        if(s == "clear"){
            list.clear();
        }
    }
    cout << "goodbye";
}