# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        largestvalues = []
        queue = []
        if root is None:
            return list()
        queue.append(root)
        while len(queue) > 0:
            largestvalues.append(find_max(queue))
            n = len(queue)
            for i in range(0,n):
                if queue[i].left != None:
                    queue.append(queue[i].left)
                if queue[i].right != None:
                    queue.append(queue[i].right)
            queue = queue[n:]
        return largestvalues

def find_max(queue):
    max_element = -(sys.maxsize-1)
    for i in range(len(queue)):
        if max_element < queue[i].val:
            max_element = queue[i].val
    return max_element
