class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    if position == 0:
        return Node(data=data, next_node=head)
    previous = head
    next = head.next
    count = 1
    while count < position:
        count += 1
        previous = next
        next = next.next
    new_node = Node(data=data, next_node=next)
    previous.next = new_node
    return head


if __name__ == '__main__':
    d = Node(data='d')
    b = Node(data='b', next_node=d)
    a = Node(data='a', next_node=b)

    head = InsertNth(a, 'c', 2)

    current = head
    while current is not None:
        print(current.data)
        current = current.next