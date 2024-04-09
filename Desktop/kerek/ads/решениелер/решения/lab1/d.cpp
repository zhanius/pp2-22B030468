#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;cin>>s;
    deque<char>dq;
    for(int i=0;i<s.size();i++){
        if(!dq.empty() and dq.back()==s[i]){
            dq.pop_back();
        }
        else{
            dq.push_back(s[i]);
        }
    }
    if(dq.empty()){
        cout<<"Yes";
    }
    else{cout<<"No";}
}