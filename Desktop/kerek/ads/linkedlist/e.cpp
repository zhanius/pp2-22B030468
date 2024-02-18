#include <iostream>
#include <map>
using namespace std;

map<string,int>m;
int cnt;
struct Node{
    string val;
    Node* next;
    Node* prev;
    Node(string val){
        this->val=val;
        this->next=NULL;
        this->prev=NULL;
    }
};

class LinkedList{
public:
    Node*head=NULL;
    Node*tail=NULL;
    void add(string val){
        Node* nw=new Node(val);
        if(head==NULL){
            head=tail=nw;
            m[nw->val]++;
        }
        else{
            tail->next=nw;
            nw->prev=tail;
            tail=nw;
            m[nw->val]++;
        }
    }
    void show(){
        for(auto i = m.rbegin();i!=m.rend();i++){
            i->second = 1;
            cnt+=i->second;
        }
        cout<<"All in all: "<<cnt<<endl;
        cout<<"Students: "<<endl;
        while(head){
            cout<<head->val<<endl;
            head=head->next;
        }
    }
};

int main(){
    int n;cin>>n;
    LinkedList l;
    while(n--){
        string s;cin>>s;
        l.add(s);
    }
    l.show();
}
