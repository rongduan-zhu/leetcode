#! /usr/bin/env python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next

        node.val = next_node.val

        if next_node.next == None:
            node.next = None
            return

        self.deleteNode(next_node)

def print_list(head):
    node = head
    vals = []

    while node != None:
        vals.append(node.val)
        node = node.next

    print vals

a = ListNode(4)
b = ListNode(3)
b.next = a
c = ListNode(2)
c.next = b
d = ListNode(1)
d.next = c

s = Solution()
s.deleteNode(d)

print_list(d)
