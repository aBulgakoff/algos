# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse_n_tree_level(root: 'Node') -> List[List[int]]:
    stack = []
    queue = deque([root]) if root else deque()

    while queue:
        len_curr_lvl = len(queue)
        stack.append(curr_lvl := [])

        for _ in range(len_curr_lvl):
            node = queue.popleft()
            curr_lvl.append(node.val)

            if node.children:
                queue.extend(node.children)
    return stack


def traverse_bin_tree_preorder(root: TreeNode) -> List[int]:
    stack, result = [(root, 0)], [[]]
    while stack and stack[-1][0]:
        node, level = stack.pop()
        result[level].append(node.val)

        if node.right:
            stack.append((node.right, level))
        if node.left:
            level += 1
            result.append([])
            stack.append((node.left, level))
    return result


def make_n_tree_nodes(tree_values: List[int]) -> List[List['Node']]:
    return [[Node(val=num, children=[]) for num in level] for level in tree_values]


def make_bin_tree_nodes(tree_values: List[List[int]]) -> List[List[TreeNode]]:
    return [[TreeNode(val) for val in level] for level in tree_values]


def link_n_tree_nodes(n_tree_nodes: List[List['Node']]) -> 'Node':
    ix = 1
    while ix < len(n_tree_nodes):
        n_tree_nodes[ix - 1][-1].children.extend(n_tree_nodes[ix])
        ix += 1
    return n_tree_nodes[0][0]


def link_bin_tree_nodes(bin_tree_nodes: List[List[TreeNode]]) -> TreeNode:
    level_ix = 1
    while level_ix < len(bin_tree_nodes):
        node_ix = 0
        while node_ix + 1 < len(level := bin_tree_nodes[level_ix]):
            level[node_ix].right = level[node_ix + 1]
            node_ix += 1
        bin_tree_nodes[level_ix - 1][-1].left = bin_tree_nodes[level_ix][0]
        level_ix += 1
    return bin_tree_nodes[0][0]


class Codec:    # NOT COMPLETE
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        levels_n_tree = traverse_n_tree_level(root)
        bin_tree_nodes = make_bin_tree_nodes(levels_n_tree)
        bin_tree_root = link_bin_tree_nodes(bin_tree_nodes)
        return bin_tree_root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        values = traverse_bin_tree_preorder(data)
        nodes = make_n_tree_nodes(values)
        root_node = link_n_tree_nodes(nodes)
        return root_node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
