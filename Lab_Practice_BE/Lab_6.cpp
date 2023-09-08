#include<bits/stdc++.h>
using namespace std;

void sum(vector<int>v1)
{
    int sum=0,i=0;
    do
    {
        sum += v1[i];
        i++;
    }
    while(i<v1.size());
    cout<<"Sum is: "<<sum<<endl;
}
void avg(vector<int>v2)
{
    int sum=0,i=0;
    do
    {
        sum += v2[i];
        i++;
    }
    while(i<v2.size());
    cout<<"Average is: "<<sum/v2.size()<<endl;

}
int main()
{
    int n,i;
    cout<<"Enter the number of array: "<<endl;
    cin>>n;
    vector<int>vec(n);
    for(i=0; i<n; i++)
    {
        cout<<"Enter number ["<<i+1<<"]";
        cin>>vec[i];
    }
    sum(vec);
    avg(vec);
}


