class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


"""
Insert Node at the begining of a linked list. Head input could be None as well for empty list.
Return back the head of the linked list in the below method.
"""

def Insert(head, data):
    if head is None:
        return Node(data)
    return Node(data=data, next_node=head)


if __name__ == '__main__':
    c = Node(data='c')
    b = Node(data='b', next_node=c)
    head = Insert(b, 'a')

    current = head
    while current is not None:
        print(current.data)
        current = current.next