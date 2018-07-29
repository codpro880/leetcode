/**
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
**/

#include <iostream>
using namespace std;
//#define NULL 0
// Typically would need a destructor here, but this is just practice problem and so we'll just leak memory for now
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
	if (head && head->next) {
	    head = swapFirstTwo(head);
	    head->next->next = swapPairs(head->next->next);
	    return head;
	}
	else {
	    return head;
	}

    }

    ListNode* swapFirstTwo(ListNode* head) {
	ListNode* cur = head;
	ListNode* n = head->next;
	if (head && head->next) {
	    ListNode* n_next = n->next;
	    n->next = cur;
	    cur->next = n_next;
	}
	return n;
    }

    void printNode(ListNode* head) {
	auto cur = head;
	while (cur) {
	    cerr << cur->val << endl;
	    cur = cur->next;
	}
    }
};

int main() {
    Solution sol = Solution();
    auto first = new ListNode(1);
    auto second = new ListNode(2);
    auto third = new ListNode(3);
    auto four = new ListNode(4);
    auto five = new ListNode(5);
    auto six = new ListNode(6);

    first->next = second;
    second->next = third;
    third->next = four;
    four->next = five;
    five->next = six;

    sol.printNode(first);
    auto result = sol.swapPairs(first);
    sol.printNode(result);
}
