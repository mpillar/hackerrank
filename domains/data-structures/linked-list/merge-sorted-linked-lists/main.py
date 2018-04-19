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


def MergeLists(head_a, head_b):

    last_node = None
    first_node = None

    while head_a is not None or head_b is not None:
        if head_a is None:
            first_node = head_b if first_node is None else first_node
            if last_node is not None:
                last_node.next = head_b
            last_node = head_b
            head_b = head_b.next
        elif head_b is None:
            first_node = head_a if first_node is None else first_node
            if last_node is not None:
                last_node.next = head_a
            last_node = head_a
            head_a = head_a.next
        elif head_a.data < head_b.data:
            first_node = head_a if first_node is None else first_node
            if last_node is not None:
                last_node.next = head_a
            last_node = head_a
            head_a = head_a.next
        else:
            first_node = head_b if first_node is None else first_node
            if last_node is not None:
                last_node.next = head_b
            last_node = head_b
            head_b = head_b.next

    return first_node
