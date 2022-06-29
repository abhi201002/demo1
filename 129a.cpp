#include <bits/stdc++.h>
using namespace std;
#define ll long long 
#define pb push_back
void solve(){
    ll n,i,m;
    cin>>n;
    ll a[n+1];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    cin>>m;
    ll b[m+1];
    for(i=0;i<m;i++){
        cin>>b[i];
    }
    sort(a,a+n);
    sort(b,b+m);
    if(a[n-1] == b[m-1]){
        cout<<"Alice\n";
        cout<<"Bob\n";
        return;
    }
    if(a[n-1]>b[m-1]){
        cout<<"Alice\n";
        cout<<"Alice\n";
        return;
    }
    cout<<"Bob\n";
    cout<<"Bob\n";
    return;
}
int main(){
    ll t;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>t;
    while(t--){
        solve();
    }
}