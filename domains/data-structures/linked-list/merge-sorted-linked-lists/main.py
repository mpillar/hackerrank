"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):

    last_node = None
    first_node = None

    while headA is not None or headB is not None:
        if headA is None:
            first_node = headB if first_node is None else first_node
            if last_node is not None:
                last_node.next = headB
            last_node = headB
            headB = headB.next
        elif headB is None:
            first_node = headA if first_node is None else first_node
            if last_node is not None:
                last_node.next = headA
            last_node = headA
            headA = headA.next
        elif headA.data < headB.data:
            first_node = headA if first_node is None else first_node
            if last_node is not None:
                last_node.next = headA
            last_node = headA
            headA = headA.next
        else:
            first_node = headB if first_node is None else first_node
            if last_node is not None:
                last_node.next = headB
            last_node = headB
            headB = headB.next

    return first_node
