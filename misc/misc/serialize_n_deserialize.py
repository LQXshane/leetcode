# 297. Serialize and Deserialize Binary Tree


'''Solution 1: simple tree traversal using queue'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        res = ""
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res += str(node.val) + " "
                q.append(node.left)
                q.append(node.right)
            else:
                res += "#" + " "
        # print res
        return res



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return []
        data = data.split()
        root = TreeNode(int(data[0]))
        i = 1
        queue = [root]
        while i < len(data):
            cur = queue.pop(0)
            if data[i] != "#":
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            if data[i + 1] != "#":
                cur.right = TreeNode(int(data[i+1]))
                queue.append(cur.right)
            i += 2
        return root
            
