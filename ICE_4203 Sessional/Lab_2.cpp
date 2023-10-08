#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,a;
    cout<<"Enter n: "<<endl;
    cin>>n;

    cout<<"Enter values then operator +: "<<endl;
    vector<double>vec(2*n);
    for(int i=0;i<2*n;i++)
    {
        cin>>vec[i];
    }
    char ch;
    cin>>ch;
    sort(vec.begin(),vec.end());
    if(ch == '+')
    {
        for(int i=0;i<2*n;i+=2)
        {
            cout<<vec[i]<<" + "<<vec[i+1]<<" = "<<vec[i]+vec[i+1]<<endl;
        }
    }
    if(ch == '-')
    {
        for(int i=0;i<2*n;i+=2)
        {
            cout<<vec[i]<<" - "<<vec[i+1]<<" = "<<abs(vec[i]-vec[i+1])<<endl;
        }
    }
    if(ch == '*')
    {
        for(int i=0;i<2*n;i+=2)
        {
            cout<<vec[i]<<" * "<<vec[i+1]<<" = "<<(vec[i]*vec[i+1])<<endl;
        }
    }
    if(ch == '/')
    {
        for(int i=0;i<2*n;i+=2)
        {
            cout<<vec[i]<<" / "<<vec[i+1]<<" = "<<(vec[i]/vec[i+1])<<endl;
        }
    }


}
