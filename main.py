# Given a binary tree, imagine you're standing to the right of the tree.
# Return an array of the values of the nodes you can see ordered from top to bottom

import queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = 0

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.elements += 1
        else:
            current = self.root

            while current:
                parent = current

                if current.data > value:
                    current = current.left

                    if current is None:
                        parent.left = node
                        return

                elif current.data < value:
                    current = current.right

                    if current is None:
                        parent.right = node
                        return
                elif current.data == value:
                    print("Unable to add duplicates")
                    return

    def print_in_order(self, node):
        if node:
            self.print_in_order(node.left)
            print(f"{node.data}")
            self.print_in_order(node.right)

    def print_post_order(self, node):
        if node:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(f"{node.data}")

    def print_preorder(self, node):
        if node:
            print(f"{node.data}")
            self.print_post_order(node.right)
            self.print_post_order(node.left)

    def right_view_bfs(self, root):
        if self.root is None:
            return []
        # Holds the resulting list with level ordered items
        result = []
        # Queue that holds all nodes in each level
        q = queue.Queue()

        # Add root to the queue
        q.put(root)

        # While there are nodes in the queue
        while q.empty() is not True:
            # The number of items in the queue
            length = q.qsize()
            # The count of how many items have been popped from the queue
            count = 0
            # List that holds values per level
            current_vals = []
            while count < length:
                # Get the node from the queue
                current_node = q.get()
                # Save its current value and add it to the placeholder list
                current_vals.append(current_node.data)

                # If there are nodes to the left or right, add them to the queue

                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)

                # Increase count
                count += 1
            # Only save the last number in each level
            result.append(current_vals[-1])

            # The following returns all numbers from the left
            # result.append(current_vals[0])

        return result

    # 1.Prioritize finding right side nodes
    # 2. Keep track of the level of our nodes

    def right_view_dfs(self, node, level, result):
        ''' Will find the right-facing nodes of the tree as if looking from the right'''
        # If the node exists
        if node:
            # If it is the first number we reach per level (PRIORITIZING GOING RIGHT FIRST)"
            if len(result) == level:
                # Add the node's value to the result list
                result.append(node.data)
            # Move to the right and then left recursively and increase the level each call. Maintain the result
            self.right_view_dfs(node.right, level + 1, result)
            self.right_view_dfs(node.left, level + 1, result)

        return result


__name__ = "__main__"

bt = BinaryTree()
bt.add(50)
bt.add(41)
bt.add(10)
bt.add(30)
bt.add(25)
bt.add(6)
bt.add(7)
bt.add(69)

print(bt.right_view_bfs(bt.root))

# print("In order:")
# bt.print_in_order(bt.root)
# print("Post-order:")
# bt.print_post_order(bt.root)
# print("Pre-order:")
# bt.print_preorder(bt.root)
print()
result = []
result = bt.right_view_dfs(bt.root, 0, result)
print(result)
