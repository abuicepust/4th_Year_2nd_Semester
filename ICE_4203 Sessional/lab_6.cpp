#include<bits/stdc++.h>
using namespace std;

void sum(vector<int>vec1)
{
    int sum=0,i=0;
    do
    {
        sum += vec1[i];
        i++;
    }while(i<vec1.size());
    cout<<"\n"<<sum;
}

void avg(vector<int>vec2)
{
    int sum=0,i=0;
    do
    {
        sum += vec2[i];
        i++;
    }while(i<vec2.size());
    cout<<"\nAverage is: "<<sum/vec2.size();
}

int main()
{
    int n;
    cout<<"Enter how many number in the array: "<<endl;
    cin>>n;

    vector<int>vec(n);
    for(int i=0;i<n;i++)
    {
        cout<<"Enter the value of "<<i<<endl;
        cin>>vec[i];
    }
    sum(vec);
    avg(vec);
}
