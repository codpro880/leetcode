/**
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
**/
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
	return search_helper(nums, target, 0, nums.size()-1);
    }

    int search_helper(vector<int>& nums, int target, int start, int stop) {
	if (nums.size() == 0) {
	    return -1;
	}
	auto first_elt = nums[start];
	auto middle_ind = (stop - start) / 2 + start;
	auto middle_elt = nums[middle_ind];
	auto last_elt = nums[stop];
	// base cases
	if (stop - start == 1) { // only two elts base case
	    if (nums[start] == target)
		return start;
	    else if (nums[stop] == target)
		return stop;
	    else
		return -1;
	}
	else if (stop - start == 0) {
	    if (nums[start] == target)
		return start;
	    else
		return -1;
	}
	else if (stop - start < 0) {
	    return -1;
	}

	// recursive cases
	if (first_elt > middle_elt) { // pivot in front, sorted in back
	    if (target > middle_elt && target <= last_elt) {
		return search_helper(nums, target, middle_ind, stop); // normal bin sort
	    }
	    else {
		return search_helper(nums, target, start, middle_ind);
	    }
	}
	else if (last_elt < middle_elt) { // pivot in back
	    if (target < middle_elt && target > last_elt) 
		return search_helper(nums, target, start, middle_ind);
	    else
		return search_helper(nums, target, middle_ind, stop);
	}
	else { // Normal bin search
	    if (target < middle_elt) {
		return search_helper(nums, target, start, middle_ind);
	    }
	    else if (target > middle_elt) {
		return search_helper(nums, target, middle_ind, stop);
	    }
	    else { // equal
		return middle_ind;
	    }
	}
    }
};

int main() {
    auto sol = Solution();
    vector<int> v{4,5,6,7,0,1,2};

    auto result = sol.search(v, 4);
    cout << "Result (0): " << result << endl;

    result = sol.search(v, 3);
    cout << "Result (-1): " << result << endl;

    result = sol.search(v, 0);
    cout << "Result(4): " << result << endl;

    vector<int> t{5,1,3};
    result = sol.search(t, 3);
    cout << "Result(2): " << result << endl;

    vector<int> z{3, 5, 1};
    result = sol.search(z, 1);
    cout << "Result(2): " << result << endl;
}
