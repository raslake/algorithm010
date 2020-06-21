###python  N 叉树的前序遍历
class Solution(object):
    def preorder(self, root):
        if not root:
            return [];
        if not root.children:
            return [root.val];
        result = [root.val];
        for child in root.children:
            result += self.preorder(child);
        return result;