#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int testcase;
    cin>>testcase;
    vector<int>v;
    while(testcase--)
    {
        int num1,num2;
        cin>>num1>>num2;
        v.push_back(num1);
        v.push_back(num2);
    }
    cout<<"Sum of two number: "<<v[0]+v[1]<<endl;
    cout<<"Sub of two number: "<<v[2]-v[3]<<endl;
    cout<<"Multiplicatio of two number: "<<v[4]*v[5]<<endl;
    cout<<"Division of two number: "<<v[6]/v[7]<<endl;

}
