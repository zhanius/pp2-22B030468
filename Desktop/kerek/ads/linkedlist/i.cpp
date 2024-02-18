#include <iostream>
using namespace std;

struct Node{
    string val;
    Node*next;
    Node*prev;
    Node(string val){
        this->val=val;
        this->prev=NULL;
        this->next=NULL;
    }
};
class LinkedList{
public:
    Node*head=NULL;
    Node*tail=NULL;
    LinkedList(){
    }
    void add_front(string val){
        Node*nw=new Node(val);
        if(head==NULL){
            head=tail=nw;
        }
        else{
            head->prev=nw;
            nw->next=head;
            head=nw;
        }
        cout<<"ok"<<endl;
    }

    void add_back(string val){
        Node*nw=new Node(val);
        if(head==NULL){
            head=tail=nw;
        }
        else{
            tail->next=nw;
            nw->prev=tail;
            tail=nw;
        }
        cout<<"ok"<<endl;
    }
    void erase_front(){
        if(head==NULL){
            cout<<"error"<<endl;
        }
        else{
            cout<<head->val<<endl;
            head=head->next;
        }
    }
    void erase_back(){
        if(head==NULL) {
            cout << "error" << endl;
            return;
        } else if(head->next == NULL){
            cout << head->val << '\n';
            head = head->next;
        }
        else{
            cout<<tail->val<<endl;
            tail = tail->prev;
        }
        tail->next = NULL;
    }
    void front(){
        if(head==NULL){
            cout<<"error"<<endl;
        }
        else{
            cout<<head->val<<endl;
        }
    }
    void back(){
        if(head==NULL){
            cout<<"error"<<endl;
        }
        else{
            cout<<tail->val<<endl;
        }
    }
    void clear() {
        Node *cur;
        if (head == NULL) {
            cout << "error" << endl;
        } else {
            while (head) {
                cur = head;
                head = NULL;
                cur = cur->next;
            }
            cout << "ok" << endl;
        }
    }
    void print(){
        Node *temp = head;
        while(temp){
            cout << temp->val << ' ';
            temp = temp->next;
        }
        cout << '\n';
    }
};

int main(){
    string s;
    LinkedList l;
    while(cin>>s){
        if(s == "add_front"){
            string s;cin>>s;
            l.add_front(s);
        }
        if(s == "add_back"){
            string s;cin>>s;
            l.add_back(s);
        }
        if(s == "erase_front"){
            l.erase_front();
        }
        if(s == "erase_back"){
            l.erase_back();
        }
        if(s == "front"){
            l.front();
        }
        if(s == "back"){
            l.back();
        }
        if(s == "clear"){
            l.clear();
        }
        if(s == "exit"){
            cout << "goodbye\n";
            break;
        }
        if(s == "print"){
            l.print();
        }
    }
}