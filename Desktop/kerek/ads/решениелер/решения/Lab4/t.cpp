#include <iostream>

using namespace std;

struct Node {
    int val;
    Node *left;
    Node *right;

    Node (int x) {
        this->val = x;
        this->left = this->right = NULL;
    }
};

struct Bst {
    Node *root;

    Bst () {
        this->root = NULL;
    }

    Node *add (Node *current, int x) {
        if (current == NULL) {
            current = new Node(x);
        }
        else if (current->val > x) {
            if (current->left == NULL)
                current->left = add(current->left, x);
            else
                add(current->left, x);
        }
        else {
            if (current->right == NULL)
                current->right = add(current->right, x);
            else
                add(current->right, x);
        }
        return current;
    }

    Node *search (Node *current, int x) {
        if (current == NULL)
            return NULL;
        if (current->val == x)
            return current;
        else if (current->val > x)
            return search(current->left, x);
        else if (current->val < x)
            return search(current->right, x);
    }

    void print_pre (Node * current){
        if(current != NULL){
            cout << current->val << " ";
            print_pre(current->left);
            print_pre(current->right);
        }
    }

    void print_in (Node * current){
        if(current != NULL){
            print_in(current->left);
            cout << current->val << " ";
            print_in(current->right);
        }
    }

    void print_post (Node * current){
        if(current != NULL){
            print_post(current->left);
            print_post(current->right);
            cout << current->val << " ";
        }
    }
};

int main() {
    Bst *B = new Bst();
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        if (B->root == NULL)
            B->root = B->add(B->root, x);
        else
            B->add(B->root, x);
    }
    cout << "Pre: \n";
    B->print_pre(B->root);
    cout << "\nIn: \n";
    B->print_in(B->root);
    cout << "\nPost: \n";
    B->print_post(B->root);
}