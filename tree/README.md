Ref:
1. LCA in BST:
http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

2. About Tree Traversal:
> There is an universal idea for preorder traversal inorder traversal and postorder traversal. For each node N, we process it as follows:

> push N in stack -> push left tree of N in stack -> pop left tree of N -> push right tree of N in stack -> pop right tree of N -> pop N
> For preorder traversal, we visit a node when pushing it in stack. For inorder traversal, we visit a node when pushing its right child in stack. for postorder traversal, we visit a node when popping it. last_pop represents the node which is popped the last time. For the top node in stack, it has three choices, pushing its left child in stack, or pushing its right child in stack, or being popped. If last_pop != top->left, meaning that its left tree has not been pushed in stack, then we push its left child. If last_pop == top->left, we push its right child. Otherwise, we pop the top node.
