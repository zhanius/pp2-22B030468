#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;cin>>t;
    while(t--){
        deque <int> dq;
        int n;cin>>n;
        dq.push_back(n);
        while(n > 0){
            dq.push_back(n - 1);
            int temp = n;
            while(temp--){
                dq.push_front(dq.back());
                dq.pop_back();
            }
            n--;
        }
        while(!dq.empty()){
            if(dq.front() != 0) cout<<dq.front()<<" ";
            dq.pop_front();
        }
        cout << '\n';
        }
        

}