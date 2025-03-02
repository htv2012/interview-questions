#!/usr/bin/env python3
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
import json

from tree import TreeNode


class Codec:
    def _serialize_to_obj(self, root):
        if root is None:
            return root
        return [
            root.val,
            self._serialize_to_obj(root.left),
            self._serialize_to_obj(root.right),
        ]

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        obj = self._serialize_to_obj(root)
        serialized_str = json.dumps(obj)
        return serialized_str

    def _deserialize_obj(self, obj):
        if obj is None:
            return None

        value, left_tree, right_tree = obj
        return TreeNode(
            value,
            left=self._deserialize_obj(left_tree),
            right=self._deserialize_obj(right_tree),
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        obj = json.loads(data)
        return self._deserialize_obj(obj)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
