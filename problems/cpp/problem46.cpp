/**
Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
**/
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
	auto result = vector<vector<int>>();
	if (nums.size() == 1) {
	    vector<int> temp{nums[0]};
	    result.push_back(temp);
	    return result;
	}
	for (auto it = nums.begin(); it != nums.end(); it++) {
	    auto without_i = _construct_without(nums, *it);
	    permute_helper(vector<int>{*it}, without_i, result);
	}
	return result;
    }

    vector<vector<int>> permute_helper(const vector<int>& start_nums_locked, const vector<int>& end_nums, vector<vector<int>>& result) {
	if (end_nums.size() == 1) {
	    auto temp = start_nums_locked;
	    temp.push_back(end_nums[0]);
	    result.push_back(temp);
	}
	else {
	    for (auto it = end_nums.begin(); it != end_nums.end(); it++) {
		auto without_i = _construct_without(end_nums, *it);
		auto temp = start_nums_locked;
		temp.push_back(*it);
		permute_helper(temp ,without_i, result);
		
	    }
	}
	return result;
    }

    vector<int> _construct_without(const vector<int>& nums, int without) {
	auto result = vector<int>();
	auto nums_copy = nums;
	for (auto it = nums_copy.begin(); it != nums_copy.end(); it++) {
	    if (*it == without) {
		nums_copy.erase(it);
		break;
	    }
	}
	return nums_copy;;
    }
};

int main() {
    auto sol = Solution();
    vector<int> v{1,2,3,4};
    auto result = sol.permute(v);

    for (auto vec : result) {
	cout << "Perm: " << endl;
	for (auto item : vec) {
	    cout << item << "," << endl;
	}
    }
}
