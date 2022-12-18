# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_len(head):
    temp = head
    out = 0
    while(temp.next != None):
        out+=1
        temp = temp.next

    return out

def get_list(head, p, out):
    while(p>=0):
        if(head == None or head.next==None):
            t = ListNode()
            out.append(t)
        else:
            out.append(head)
        head = head.next
        p-=1
    return out, head



def splitListToParts(head: ListNode, k: int) -> list[ListNode]:
    l = get_len(head)
    temp = head
    out = []
    for i in range(k, 0, -1):
        p = math.ceil(l/k)
        out, temp = get_list(temp, p, out)


    return out
        



    

if __name__ == "__main__":
