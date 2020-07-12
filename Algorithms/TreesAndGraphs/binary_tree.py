class binary_tree(object):
    """This class holds the data structure for a binary tree"""
   
    def __init__(self, current, left=None, right=None):
        self.current_node_data = current
        self.left_node = left
        self.right_node = right
        self.is_visited = False
        self.depth = 0
   
    def print_self_pre_order(self):
        node = self
        print(node.current_node_data)

        if node.left_node != None:
            node.left_node.print_self_pre_order()
    
        if node.right_node != None:
            node.right_node.print_self_pre_order()

    def print_self_in_order(self):
        node = self
        
        if node.left_node != None:
            node.left_node.print_self_in_order()
    
        print(node.current_node_data)

        if node.right_node != None:
            node.right_node.print_self_in_order()
