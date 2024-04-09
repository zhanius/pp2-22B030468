#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Node {
    string val;
    Node *next;

    Node (string x) {
        this->val = x;
        this->next = NULL;
    }
};

struct LL {
    Node *head;
    Node *cur;
    int size;

    LL () {
        this->head = NULL;
        this->cur = this->head;
        this->size = 0;
    }

    LL (string val) {
        this->head = new Node(val);
        this->cur = this->head;
        this->size = 1;
    }

    void add (string val) {
        cur->next = new Node(val);
        cur = cur->next;
        size++;
    }

    void print () {
        Node *tmp = head;
        cout << size << '\n';
        while (tmp != NULL) {
            cout << tmp->val << '\n';
            tmp = tmp->next;
        }
    }
};

int LPS (string patt, string s, int m, int n) {
    int len = 0;
    int i = 1;
    while (i < m && len < n) {
        if (s[i] == patt[len]) {
            len++;
            i++;
        }
        else if (len != 0) {
            len = 0;
        }
        else {
            i++;
        }
    }
    return len;
}

int main() {
    string s; cin >> s;
    s[0] = tolower(s[0]);
    int n; cin >> n;
    int max = -1;
    LL list;
    for (int i = 0; i < n; i++) {
        string t; cin >> t;
        string tmp = t;
        tmp[0] = tolower(t[0]);
        int length = LPS(tmp, s,  s.size(), tmp.size());
        if (max < length) {
            max = length;
            list = LL(t);
        }
        else if (max == length) {
            list.add(t);
        }
    }
    list.print();
}