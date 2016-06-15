class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def ReversePrint(head):
    output = []
    current = head
    while current is not None:
        output.append(current.data)
        current = current.next
    for data in reversed(output):
        print(data)


if __name__ == '__main__':
    c = Node(data='c')
    b = Node(data='b', next_node=c)
    a = Node(data='a', next_node=b)
    ReversePrint(a)