def in_order(t):
    """
    Yields the entries of a valid binary search tree in sorted order.

    >>> b = BTree(5, BTree(3, BTree(2), BTree(4)), BTree(6))
    >>> list(in_order(b))
    [2, 3, 4, 5, 6]
    >>> list(in_order(bst([1, 3, 5, 7, 9, 11, 13])))
    [1, 3, 5, 7, 9, 11, 13]
    >>> list(in_order(BTree(1)))
    [1]
    """
    "*** YOUR CODE HERE ***"

def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    "*** YOUR CODE HERE ***"

class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(Tree(1))
    1
    >>> print_tree(Tree(1, [Tree(2)]))
    1
      2
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(t.root))
    for b in t.branches:
        print_tree(b, indent + 1)

# Binary trees

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.root)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.root, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.root, left, right)
# Binary search trees

def bst(values):
    """Create a balanced binary search tree from a sorted list.

    >>> bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left, right = bst(values[:mid]), bst(values[mid+1:])
    return BTree(values[mid], left, right)
