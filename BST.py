class Node:
    """
    A class representing a node in a binary search tree.
    Each node contains a query string, a list of URLs, and references to its parent and child nodes.
    """
    def __init__(self, query: str, urls: list):
        """
        Initialize a new Node with a query string, a list of URLs, and no parent or child nodes.
        """
        self.query = query
        self.urls = urls
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self) -> str:
        """
        Return a string representation of the Node, which is its query string.
        """
        return f'{self.query}'

class BinarySearchTree:
    """A class representing a binary search tree.The tree is initialized with no root node.
    """
    def __init__(self):
        """Initialize a new BinarySearchTree with no root node."""
        self.root = None

    def insert(self, query: str, urls: list) -> None:
        """Insert a new Node into the tree with the given query string and list of URLs."""
        new = Node(query, urls)
        if not self.root:
            self.root = new
        else:
            self.inserting(self.root, new)

    def inserting(self, node, new):
        """Helper method for insert. Inserts a new Node into the tree at the correct position."""
        while True:
            if new.query < node.query:
                if not node.left:
                    node.left = new
                    new.parent = node
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = new
                    new.parent = node
                    break
                else:
                    node = node.right

    def search(self, query: str) -> Node or None:
        """Search the tree for a Node with the given query string.
        Returns the Node if found, or None if not found.
        """
        return self.searching(self.root, query)

    def searching(self, node, query):
        """Helper method for search. Recursively searches the tree for a Node with the given query string."""
        if not node: return None;
        if query == node.query: return node.urls;
        elif query < node.query: return self.searching(node.left, query);
        else: return self.searching(node.right, query)

    def height(self) -> int:
        """
        Return the height of the tree.
        The height of a tree is the maximum number of edges in a path from the root node to a leaf node.
        """
        if self.root is None: return 0;
        stack = [(self.root, 1)]
        max_height = 0
        while stack:
            node, height = stack.pop()
            max_height = max(max_height, height)
            if node.left: stack.append((node.left, height + 1));
            if node.right: stack.append((node.right, height + 1));
        return max_height

