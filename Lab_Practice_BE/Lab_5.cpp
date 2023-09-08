#include<bits/stdc++.h>
using namespace std;

int fact(int n)
{
    if(n == 1)
        return 1;
    else
        return n*fact(n-1);
}

int main()
{
    int n,i;
    cout<<"Enter the number: "<<endl;
    cin>>n;

    //for(i=n;i>=1;i--)
    //{
        //cout<<"iteration: "<<i<<" * "<<fact<<" = ";
        //fact = fact * i;
        //cout<<fact<<endl;
    //}
    cout<<"Factorial of "<<n<<" is: "<<fact(n);
}
