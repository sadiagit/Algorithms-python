import TreesAndGraphs
import SortingAndSearching


#TreesAndGraphs
btree = TreesAndGraphs.binary_tree(5,TreesAndGraphs.binary_tree(3, 
                                    TreesAndGraphs.binary_tree(1),TreesAndGraphs.binary_tree(2)),
                                   TreesAndGraphs.binary_tree(8,TreesAndGraphs.binary_tree(6), TreesAndGraphs.binary_tree(9)))

#btree.print_self_in_order()
#btree.print_self_pre_order()

#TreesAndGraphs.list_depths().list_each_depth(btree)


#sorting and searching

#implementing merge sort
SortingAndSearching.merge_sort([2,4,6,3,5,1])

# Reduce the array by deleting elements which are greater than all elements to its left 
SortingAndSearching.merge_del([2,4,3,1])
SortingAndSearching.merge_del([5,4,3,2,1])



          


