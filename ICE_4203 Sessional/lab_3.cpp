#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str1,str2;
    cout<<"Enter string 1: "<<endl;
    getline(cin,str1);
    //str2 = str1;
    //reverse(str2.begin(),str2.end());

    //int len = str1.size();
    int i=0,len=0,j=0;
    while(str1[i] != '\0')
    {
        i++;
        len++;
    }
    for(j=0,i=len-1;i>=0;i--,j++)
    {
        str2[j]=str1[i];
    }
    str2[j] = '\0';
    cout<<"String 1: "<<str1<<endl;
    cout<<"String 2: "<<str2<<endl;
    if(str1 == str2)
    {
        cout<<"Palindrome"<<endl;
    }
    else
        cout<<"Not a Palindrome";
}
