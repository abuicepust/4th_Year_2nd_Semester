#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n1,n2;
    cout<<"Enter the number operator and ="<<endl;
    cin>>n1;
    char op;
    cin>>op;
    cin>>n2;
    char ch;
    cin>>ch;
    while(ch == '=')
    {
        if(op == '+')
        {
            cout<<n1<<" + "<<n2<<" = "<<n1+n2<<endl;
            break;
        }
    }
}
