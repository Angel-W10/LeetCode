# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import floor


class Solution:
    def rotateRight(self, head, k: int):
        '''
        option 1: 
        subtract k from the len fo list to reduce the number of rotations
        but to get len, O(n)

        option 2:
        just rotate k times

        but to rotate get the last node and add it as the first
        i.e.
        second_last, last, temp = head
        last.next = temp
        second_last.next = None

        each rotation = O(n)

        so we do option 1, 
        as if k = len(list):
            new_list = old_list
        '''
        def get_second_last_node(head):
            temp = head
            while temp.next!=None and temp.next.next != None:
                temp = temp.next

            return temp
        # get the length of the list to reduce the number of rotations:
        # + 
        # get the last and the second last node
        
        temp = head
        n = 0

        while temp!=None:
            n+=1
            temp = temp.next

        if n==0 or n==1:
            return head



        # print(n)

        # reducing the number of rotations to process
        if k > n:
            # check how many ns are there in k and then delete it as it will give out the original list
            k = k - (floor(k/n)*n)


        new_head, temp_head = head, head
        while k!=0:
            # rotate

            # get the last, second_last
            second_last = get_second_last_node(temp_head)
            last = second_last.next

            # last.next = temp_head
            # second_last.next = None
            last.next = temp_head
            second_last.next = None

            # new_head, temp_head = last, last
            new_head, temp_head = last, last

            k-=1

        return new_head
        