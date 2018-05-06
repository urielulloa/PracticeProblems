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

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None or k == 0 or head.next is None:
            return head
        
        
        #Loop to get the length of the linked-list. O(n)
        #This loop is necessary to compute k%length of list which tells us whihch element is the last element in our list
        current = head
        length = 1
        while current.next is not None:
            length +=1
            current= current.next
        end = current
            
        #Second loop to find the the cutt-off point of the list. < O(n-k%n)
        count = 1   
        current = head
        while count < length - k%length:
            current = current.next
            count += 1 
        #Found the cutt-off point
        #Make the current element the end of the list and place the elements that used to be next at the front of the list
        end.next = head
        front = current.next
        current.next = None
        
        return front
        
