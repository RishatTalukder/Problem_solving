#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int profit = 0;
        int maxx = 0;

        for(int i =1; i < prices.size(); i++){
            if (prices[i] < buy){
                buy = prices[i];
            }
            else {
                profit = prices[i] - buy;
                maxx = max(profit,maxx);
            }
        }
    }
};