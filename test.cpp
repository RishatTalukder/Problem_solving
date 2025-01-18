#include<iostream>

using namespace std;

int main()
{
    int arr[5] = {1,2,3,4,5};
    int target = 13;
    int len = sizeof(arr)/sizeof(arr[0]); // to find the lenngth of a array we use this formula
    for(int i=0; i <=len-1; i++){
        if(arr[i]==target){
            cout<<i<<endl;
            return 0;
        }
    }
    cout<<"target not found"<<endl;
} // namespace std;
