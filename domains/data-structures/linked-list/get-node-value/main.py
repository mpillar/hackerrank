def get_node(head, position_from_tail):
    """
    Given a singly linked list, find the value of the node a given number
    of positions from the tail of the list
    """
    if head is None:
        return 0
    
    list_size = 0
    current_node = head
    while current_node is not None:
        list_size += 1
        current_node = current_node.next
        
    desired_index = list_size - position_from_tail - 1
    current_index = 0
    current_node = head
    
    while current_index != desired_index:
        current_index += 1
        current_node = current_node.next
        
    return current_node.data
