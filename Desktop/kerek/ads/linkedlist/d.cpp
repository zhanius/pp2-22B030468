#include <iostream>
#include <map>
using namespace std;

map <int,int> m;
int cnt;
struct Node {
    int val;
    Node *next;
    Node *prev;
    Node(int val) {
        this->val = val;
        this->prev = NULL;
        this->next = NULL;
    }
};

class LinkedList {
public:
    Node *head = NULL;
    Node *tail = NULL;
    void add(int val) {
        Node *nw = new Node(val);
        if (head == NULL) {
            head = tail = nw;
            m[nw->val]++;
        } else {
            tail->next = nw;
            nw->prev = tail;
            tail = nw;
            m[nw->val]++;
        }
    }
    void maxvalue() {
        while(head){
            cnt = max(m[head->val],cnt);
            head=head->next;
        }
    }
};

int main() {
    int n;
    cin >> n;
    LinkedList l;
    while (n--) {
        int x;
        cin >> x;
        l.add(x);
    }
    l.maxvalue();
    for(auto it = m.rbegin(); it != m.rend();++it){
        if(it->second == cnt){
            cout << it->first << ' ';
        }
    }
}
