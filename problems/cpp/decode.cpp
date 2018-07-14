/**
Given a string of chars 1-9, make a function to return how many ways to "decode" a message.
To decode a message, we use a simple decoding where each number can map to it's corresponding position in the alphabet.

"1" -> a
"2" -> b
...
"26" -> z

Example:

input = "12"
output = 2
Reasoning:
"12" can be decoded as "ab" or as "l" (since l is the 12th letter of the alphabet).

 **/
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

bool is_valid(string);
static size_t sum = 0;

size_t num_ways(string data) {
    if (data == "") {
	return 1;
    }
    else if (data.length() == 1) {
	return 1;
    }
    else {
	auto first_way = num_ways(data.substr(1, data.length()-1));
	auto second_way = num_ways(data.substr(2, data.length()-2));
	if (is_valid(data.substr(0, 2))) {
	    cout << "Returning both..." << endl;
	    return first_way + second_way;
	}
	else {
	    return first_way;
	}
    }
}

bool is_valid(string data) {
    auto x = unordered_set<string>{"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"};
    return x.count(data) == 1;
}

int main() {
    string test = "1234";
    auto result = num_ways("1234");
    cout << "result: " << result << endl;
}
