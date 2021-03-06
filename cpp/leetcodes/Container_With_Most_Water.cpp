/*
 *
 * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 * Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Show Tags
Show Similar Problems


 */



#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <queue>
#include <stack>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int area = 0;
        while (l < r){
            area = max(area, min(height[l], height[r])*(r-l));
            if (height[l] < height[r]){
                l++;
            }else{
                r--;
            }
        }
        return area;
    }
};

int main(){
    Solution s;
    auto v = vector<int>{2,1};
    cout << s.maxArea(v) << endl;

    v = vector<int>{2,1,1,3,2,4,2,1};
    cout << s.maxArea(v) << endl;

}