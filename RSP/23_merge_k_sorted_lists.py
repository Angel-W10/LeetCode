# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_min(self, vals):
        n = len(vals)
        m_index = 0
        mini = 9999999
        min_node = vals[0]
        for i in range(n):
            if vals[i]!=None and vals[i].val < mini:
                mini = vals[i].val
                min_node = vals[i]
                m_index = i
        return min_node, m_index


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        lists = [[1,4,5],[1,3,4],[2,6]]

        p1 = 5
        p2 = None
        p3 = 6

        out->p1(1)->p2(1)->p3(2)->p2(3)->p1(4)->p2(4)->p1(5)->p3(6)

        until p1, p2 and p3 != None
        get a pointer at the head of each list in lists
        create a dummy head, 
        get the smallest pointer value and add it to dummy.next
        move the pointer to the next value

        return dummy.next

        time: O(max(lists.length))
        Space: O(sum(lists.length))
        '''

        n = len(lists)
        node_pointers = [None]*n

        for i in range(n):
            node_pointers[i] = lists[i]

        dummy_head = ListNode(-1)
        temp = dummy_head


        while node_pointers != [None]*n:
            # get the min node_pointers[i].val
            min_node, min_index = self.get_min(node_pointers)

            # put it at temp.next
            temp.next = min_node

            # node_pointers[i] = node_pointers[i].next
            node_pointers[min_index] = node_pointers[min_index].next

            # temp = temp.next
            temp = temp.next



        return dummy_head.next