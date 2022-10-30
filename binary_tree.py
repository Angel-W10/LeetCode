'''class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if(self.root):
            start = self.root
            
            return self.preorder_search(start, find_val)
        
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if(self.root):
            start = self.root
            trav = []
            return self.preorder_print(start, trav)
        
        return ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        temp = start
        if(temp.value==find_val):
            return True
        if(temp.left):
            if(temp.left.value==find_val):
                return True
            else:
                return self.preorder_search(temp.left, find_val)
                
        if(temp.right):
            if(temp.right.value==find_val):
                return True
            else:
                return self.preorder_search(temp.right, find_val)
        
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        temp = start
        traversal.append(temp.value)
        
        if(temp.left):
            self.preorder_print(temp.left, traversal)
            
        if(temp.right):
            self.preorder_print(temp.right, traversal)
        
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()'''



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if(self.value):
            if(value < self.value):
                if(self.left is None):
                    self.left = Node(value)
                else:
                    self.left.insert(value)

            if(value>self.value):
                if(self.right is None):
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
        

    def pre_order_print(self):
        print(self.value)

        if(self.left):
            self.left.pre_order_print()
        
        if(self.right):
            self.right.pre_order_print()


    def in_order_print(self):
        
        if(self.left):
            self.left.in_order_print()
        
        print(self.value)

        if(self.right):
            self.right.in_order_print()

    def post_order_print(self):
        if(self.left):
            self.left.post_order_print()

        if(self.right):
            self.right.post_order_print()

        print(self.value)




if __name__ == "__main__":
    mytree = Node(20)
    mytree.insert(17)
    mytree.insert(18)
    mytree.insert(19)
    mytree.insert(21)
    mytree.insert(22)
    mytree.insert(35)
    print("pre-order: ")
    mytree.pre_order_print()

    print("in-order: ")
    mytree.in_order_print()

    print("post-order: ")
    mytree.post_order_print()
