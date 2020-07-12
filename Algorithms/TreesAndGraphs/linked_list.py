class linked_list(object):
    """This class holds the data structure for linked list"""

    def __init__(self, current, next=None):
        self.current_node_data = current
        self.next = next

    def append(self, data):
        self.next = linked_list(data,None)
        return self.next



