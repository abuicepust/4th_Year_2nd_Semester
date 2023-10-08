#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,fact=1;
    cout<<"Enter the number: "<<endl;
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cout<<fact<<" * "<<i<<" is ";
        fact = fact*i;
        cout<<fact<<endl;
    }
    cout<<"Value of factorial "<<n<<" is: "<<fact<<endl;
}
