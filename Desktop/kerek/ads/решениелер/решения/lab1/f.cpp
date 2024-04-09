#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n){
    for(int i=2;i<=n/2;i++)
        if(n%i==0)
            return false;
    return true;
}

int main(){
    int n;cin>>n;
    int prime,cnt=0;
    stack<int>st;
    for(int i=2;cnt<n;i++){
        if(isPrime(i)){
            prime=i;
            cnt++;
            st.push(i);
        }
    }
    cout<<st.top();
}