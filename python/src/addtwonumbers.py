"""
Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode:
    """
    Definition for singly-linked list.

    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.__to_str()

    def __to_str(self):
        if self.next:
            return str(self.val) + '->' + self.next.__to_str()
        else:
            return str(self.val)


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        num1 = self.num_of(l1)
        num2 = self.num_of(l2)

        sum = num1 + num2

        return self.as_reversed_linkedlist(sum)

    def num_of(self, l):
        num = l.val
        i = 1
        while l.next:
            num += i * 10 * l.next.val
            l = l.next
            i *= 10

        return num

    def as_reversed_linkedlist(self, num):
        ratio = 10

        if num < 10:
            return ListNode(num)

        header = None
        while num > 0:
            node = ListNode(num % ratio)
            if not header:
                header = node
                list = header
            else:
                list.next = node
                list = list.next

            num /= ratio

        return header


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(1)
    l1.next.next = ListNode(6)
    l2 = ListNode(0)

    print Solution().addTwoNumbers(l1, l2)






