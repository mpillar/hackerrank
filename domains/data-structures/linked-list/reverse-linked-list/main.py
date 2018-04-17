"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    if head is None:
        return None

    node_current = head
    node_next = head.next

    result = None
    node_current.next = None

    while node_next is not None:
        # Make connection
        new_node_next = node_next.next
        node_next.next = node_current
        # Move to next
        node_current = node_next
        node_next = new_node_next

        result = node_current
        print(result.data)

    return result
