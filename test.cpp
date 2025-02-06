#include<iostream>
#include<unordered_map>
using namespace std;

int main()
{
    int arr[7] = {1,2,3,3,5,3,3};
    unordered_map<int, int> counter;
    int n = sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<n;i++){
        if(counter.count(arr[i]) == 0){
            counter[arr[i]] = 1;
        }
        else{
            counter[arr[i]]++;
        }
    }
    for(auto i:counter){
        if (i.second > n/2){
            cout << i.first << endl;
        }
        else{
            cout << "No Majority Element" << endl;
        }
    }
} // namespace std;
