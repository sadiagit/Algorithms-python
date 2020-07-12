import TreesAndGraphs



btree = TreesAndGraphs.binary_tree(5,TreesAndGraphs.binary_tree(3, 
                                    TreesAndGraphs.binary_tree(1),TreesAndGraphs.binary_tree(2)),
                                   TreesAndGraphs.binary_tree(8,TreesAndGraphs.binary_tree(6), TreesAndGraphs.binary_tree(9)))

#btree.print_self_in_order()
#btree.print_self_pre_order()

TreesAndGraphs.list_depths().list_each_depth(btree)