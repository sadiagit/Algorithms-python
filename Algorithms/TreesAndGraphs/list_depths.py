import threading
import TreesAndGraphs
import queue


class list_depths(object):
    """Given a binary tree, this class designs an algorithm which creates a linked list of all the nodes
at each depth
It uses a queue to store each neighbouring nodes to be explored next (BFS)
Every time it explores a node it also sets its depth.
When a node is dequed and its depth higher than the current depth, a new linked list for a new level is created
if the depth of the node is same as current depth, linked list will grow for the same level
Its time and space complexity is O(n) where n is the number of nodes. 
I can improve it to O(logn) by creating/appending the list as soon as the node is explored and only looping until the node's left or right child has children. 
This way I only need to loop through the 1/2 of the nodes i.e. no need to continue the loop for the leaf nodes that has the highest number of nodes.
"""
      
    def list_each_depth(self,btree):
        
        linked_lists = []
        
        q = queue.Queue()
        q.put(btree)

        list = TreesAndGraphs.linked_list(btree.current_node_data)
        linked_lists.append(list)
        
        list = None
        current_depth = 1
        while(not q.empty()):

            node = q.get()    
            
            # 
            #  create a linked
            # list for this node
            if node.depth > current_depth:
                list = TreesAndGraphs.linked_list(node.current_node_data)
                current_depth = node.depth
                linked_lists.append(list)
            elif list != None:
                list = list.append(node.current_node_data)
           
            # explore the node's left and right children and add new linked
            # list for this level
            if node.left_node != None:
              node.left_node.depth = current_depth + 1
              #queue the children so their children can be explored
              q.put(node.left_node)
            if node.right_node != None:
              node.right_node.depth = current_depth + 1
              q.put(node.right_node)
           
        
        for list in linked_lists:
            print(str(list.current_node_data), end= '\n' if list.next == None else '' ),
            while(list.next != None):
                list = list.next
                print('->'+ str(list.current_node_data),end='\n' if list.next == None else ''),
      
               

      

            
   
     
           
           

           





