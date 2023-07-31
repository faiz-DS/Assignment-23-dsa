from collections import defaultdict, deque

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return

    queue = deque([(root, 0)])
    horizontal_distance_map = defaultdict(lambda: None)

    while queue:
        node, horizontal_distance = queue.popleft()
        horizontal_distance_map[horizontal_distance] = node.data

        if node.left:
            queue.append((node.left, horizontal_distance - 1))

        if node.right:
            queue.append((node.right, horizontal_distance + 1))

    return [value for key, value in sorted(horizontal_distance_map.items())]


# Test cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(20)
    root1.left = Node(8)
    root1.right = Node(22)
    root1.left.left = Node(5)
    root1.left.right = Node(3)
    root1.right.right = Node(25)
    root1.left.right.left = Node(10)
    root1.left.right.right = Node(14)

    print("Output for Example 1:", bottom_view(root1))  # Output: [5, 10, 3, 14, 25]

    # Example 2
    root2 = Node(20)
    root2.left = Node(8)
    root2.right = Node(22)
    root2.left.left = Node(5)
    root2.left.right = Node(3)
    root2.right.left = Node(4)
    root2.right.right = Node(25)
    root2.left.right.left = Node(10)
    root2.left.right.right = Node(14)

    print("Output for Example 2:", bottom_view(root2))  # Output: [5, 10, 4, 14, 25]
