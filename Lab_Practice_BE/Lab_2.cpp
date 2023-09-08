#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,i;
    cout<<"Enter the number n: "<<endl;
    cin>>n;

    vector<int>vec(2*n);
    cout<<"Enter numbers: "<<endl;
    for(i=0;i<2*n;i++)
    {
        cin>>vec[i];
    }
    char ch;
    cin>>ch;
    if(ch == '+')
    {
        for(i=0;i<2*n;i+=2)
        {
            cout<<vec[i]<<" + "<<vec[i+1]<<" = "<<vec[i]+vec[i+1]<<endl;
        }
    }
}
