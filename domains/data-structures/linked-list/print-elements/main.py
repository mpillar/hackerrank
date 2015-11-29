class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
def print_list(head):
    """
    Print elements of a linked list on console head input could be None as well
    for empty list.
    """
    current = head
    while current is not None:
        print(current.data)
        current = current.next

if __name__ == '__main__':
    c = Node(3, None)
    b = Node(2, c)
    a = Node(1, b)

    print_list(a)
