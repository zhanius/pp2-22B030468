#include <bits/stdc++.h>
using namespace std;

int main(){
    string s1,s2;cin>>s1>>s2;
    deque<char>dq1;
    deque<char>dq2;
    for(char j : s1){
        if(!dq1.empty() and j == '#'){
            dq1.pop_back();
        }
        else{
            dq1.push_back(j);
        }
        }
    for(char i : s2){
        if(!dq2.empty() and i == '#'){
            dq2.pop_back();
        }
        else{
            dq2.push_back(i);
        }
    }
    while(!dq1.empty() or !dq2.empty()){
        if(dq1.front()==dq2.front()){
            dq1.pop_front(); dq2.pop_front();
        }
        else{
            cout<<"No"; return 0;
        }
    }
    if(dq1.empty() and dq2.empty()){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }
}