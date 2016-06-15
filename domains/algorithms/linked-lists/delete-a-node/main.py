class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    if head is None:
        return None
    if position == 0:
        return head.next
    previous = head
    current = head.next
    count = 1
    while count < position:
        count += 1
        previous = current
        current = current.next
    if current is None:
        previous.next = None
    else:
        previous.next = current.next
    return head

if __name__ == '__main__':
    c = Node(data='c')
    b = Node(data='b', next_node=c)
    a = Node(data='a', next_node=b)

    head = Delete(a, 1)

    current = head
    while current is not None:
        print(current.data)
        current = current.next