#include<bits/stdc++.h>
using namespace std;

int main()
{
    string str1,str2;

    cout<<"Enter the first String :"<<endl;
    cin>>str1;
    //cout<<str1;
    str2 = str1;
    reverse(str2.begin(),str2.end());
    if(str1 == str2)
    {
        cout<<"Palindrome"<<endl;
    }
    else
    {
        cout<<"Not a palindrome"<<endl;
    }
}
