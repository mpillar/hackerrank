"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    currentA = headA
    currentB = headB
    while currentA is not None and currentB is not None:
        if currentA.data != currentB.data:
            return 0
        currentA = currentA.next
        currentB = currentB.next
    return 1 if currentA is None and currentB is None else 0
