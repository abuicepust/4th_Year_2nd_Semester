#include<bits/stdc++.h>
using namespace std;

int main()
{
    //cout<<"Hello world";
    double a, b;
    char oprtr,pre;
    cout<<"Enter a number then operator then number then  = : "<<endl;
    cin>>a;
    cin>>oprtr;
    cin>>b;
    cin>>pre;
    if(a<b){swap(a,b);}
    while(pre == '=')
    {
        if(oprtr == '+')
        {
            cout<<a<<" + "<<b<<" = "<<a+b;
            break;
        }
        else if(oprtr == '-')
        {
            cout<<a<<" - "<<b<<" = "<<a-b;
            break;
        }
        else if(oprtr == '*')
        {
            cout<<a<<" * "<<b<<" = "<<a*b;
            break;
        }
        else if(oprtr == '/')
        {
            cout<<a<<" / "<<b<<" = "<<a/b;
            break;
        }
        else if(oprtr == '%')
        {
            cout<<a<<" % "<<b<<" = "<<int(a)%int(b);
            break;
        }
        else
        {
            cout<<"Invalid Operator"<<endl;
            break;
        }
    }
}
