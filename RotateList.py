"""
Runtime: O(n).
Space: O(1), no data structures created.

Problem can be found at this link: https://leetcode.com/problems/rotate-list/description/

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None or k == 0 or head.next is None:
            return head
        
        current = head
        length = 1
        
        #Loop to get the length of the linked-list. O(n)
        #This loop is necessary to compute k%length of list which tells us whihch element is the alst element in our list
        while current.next is not None:
            length +=1
            current= current.next
        
        count = 1   
        current = head
        front = head
         
        #Second loop through the list to modify list into the solution. O(n)
        while count <= length:
            #This will be the last element in our solution
            if count == length - k%length:  
                end = current
            #Cut of the list from the element we marked as the end and place it at the front of the list.
            if count == length:
                current.next = front
                front = end.next
                end.next = None
            
            current = current.next
            count += 1

        return front 
        
