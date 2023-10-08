#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int testcase;
    cin>>testcase;
    vector<int> v;
    while(testcase--)
    {
        int Num1,Num2;
        cin>>Num1>>Num2;
        v.push_back(Num1);
        v.push_back(Num2);
    }
    cout<<"Sum of Two number : "<<v[0]+v[1]<<endl;
    cout<<"Subtraction of Two number: "<<v[2]-v[3]<<endl;
    cout<<"Multiplication of Two number: "<<v[4]*v[5]<<endl;
    cout<<"Division of Two number : "<<v[6] / v[7]<<endl;
    return 0;
}
