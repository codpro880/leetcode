#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
	if (needle == "") {
	    return 0;
	}
	for (int i = 0; i < haystack.length(); i++) {
	    if (haystack[i] == needle[0]) {
		int needle_len = needle.length();
		if (haystack.substr(i, needle_len) == needle) {
		    return i;
		}
	    }
	}
	return -1;
    }
};

int main() {
    Solution sol = Solution();
    cout << "Should be 2: " << sol.strStr("hello", "ll") << std::endl;

    cout << "Should be -1: " << sol.strStr("aaaa", "bba") << std::endl;
}
