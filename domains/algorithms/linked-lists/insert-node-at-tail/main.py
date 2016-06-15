class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


"""
Insert Node at the end of a linked list. Head pointer input could be None as well for empty list.
Return back the head of the linked list.
"""

def Insert(head, data):
    if head is None:
        return Node(data)
    current = head
    while current.next is not None:
        current = current.next
    new_node = Node(data)
    current.next = new_node
    return head


if __name__ == '__main__':
    c = Node(data='c')
    b = Node(data='b', next_node=c)
    a = Node(data='a', next_node=b)
    Insert(a, 'd')

    current = a
    while current is not None:
        print(current.data)
        current = current.next