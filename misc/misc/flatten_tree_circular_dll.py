# https://www.youtube.com/watch?v=Dte6EF1nHNo
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=289584&extra=page%3D1%26filter%3Dsortid%26sortid%3D192%26sortid%3D192

# class TreeNode():
#     def __init__(self, x):
#         self.value = x
#         self.left = None
#         self.right = None

def treeToList(root):
    if not root: return None
    left = treeToList(root.left)
    right = treeToList(root.right)
    root.left = root
    root.right = root

    root = concat(left, root)
    root = concat(root, right)
    return root

def concat(a, b):
    if not a: return b
    if not b: return a

    a_end = a.left
    b_end = b.left

    a.left = b_end
    b_end.right = a
    a_end.right = b
    b.left = a_end

    return a
