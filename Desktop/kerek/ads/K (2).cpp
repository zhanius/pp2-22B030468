#include <bits/stdc++.h> 
using namespace std; 
 
struct Node{ 
    char val; 
    Node * next; 
    Node(char val) { 
        this->val = val; 
        next=NULL; 
    } 
}; 
 
class LinkedList{ 
public: 
    int a[26]; 
    Node * head; 
    LinkedList() { 
        for (int i = 0; i < 26; i ++) { 
            a[i] = 0; 
        } 
        head=NULL; 
    } 
    void push(char val) { 
        Node * newNode = new Node(val); 
        if(head == NULL) { 
            cout << val << " "; 
            a[val - 'a']++; 
            head = newNode; 
        } 
        else{ 
            Node * cur = head; 
            char result = '!'; 
            a[val - 'a']++; 
            bool ok = false; 
            while(cur!=NULL){ 
                if (a[cur -> val - 'a'] == 1 && !ok){ 
                    ok = 1; 
                    result = cur -> val; 
                } 
                if(cur->next==NULL) { 
                    if (a[val - 'a'] == 1 && !ok) result = val; 
                    cur->next=newNode; 
                    break; 
                } 
                cur=cur->next; 
            } 
            if (result == '!') cout << -1 << " "; 
            else cout << result << " "; 
        } 
 
    } 
}; 
 
void solve() { 
    LinkedList list; 
    int n; 
    cin >> n; 
    for(int i = 0; i < n;i++){ 
        char x; 
        cin>>x; 
        list.push(x); 
    } 
    cout << endl; 
} 
 
int main() { 
    int t; 
    cin>>t; 
    while(t--) { 
        solve(); 
    } 
}