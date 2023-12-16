
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def printTree(self):
        #Printing nodes relative to each other while printing the tree. 
        if self.left_child:
            print(self.left_child.value,"<--",self.value)
            self.left_child.printTree()

        if self.right_child:
            print(self.value,"-->",self.right_child.value)
            self.right_child.printTree()

    def insert_node(self, value):
        #If the value belongs in the left-subtree. 
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)

        #There is no existing left-node so this takes the place of the left-subtree.  
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)

        #If the value belongs in the right sub-tree. 
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)

        #There is no existing right-node so this takes the place of the right-subtree. 
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value, path):

        #If the value is lesser than current node, append steps to path and recurse on left-subtree. 
        if value < self.value and self.left_child:
            path.append(str(self.value))
            path.append("Left")
            return self.left_child.find_node(value,path)

        #If the value is greater than current node, append steps to path and recurse on right-subtree. 
        if value > self.value and self.right_child:
            path.append(str(self.value))
            path.append("Right")
            return self.right_child.find_node(value,path)

        if value == self.value:
            return path
        else:
            return False

    def remove_node(self, value, parent):

        #If value is in the left-subtree. 
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)

        #Value doesn't exist. 
        elif value < self.value:
            return False

        #If value is in the right-subtree. 
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)

        #Value doesn't exist. 
        elif value > self.value:
            return False

        #We found the value. 
        else:
            #Node: Leaf Node, Left-Child of the Parent.
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            #Node: Leaf Node, Right-Child of the Parent.
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            #Node: Has a Left-Child Only, Is a Left-Child
            # Then, removes the node, and connects parent to node's left-child. 
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            #Node: Has a Left-Child Only, Is a Right-Child.
            # Then, removes the node, and connects parent to node's left-child. 
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            #Node: Has a Right-Child Only, Is a Left-Child.
            # Then, removes the node, and connects parent to node's right-child.
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            #Node: Has a Right-Child Only, Is a Right-Child.
            #Then, removes the node, and connects parent to node's right-child.
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            #Node: Has Two Children.
            else:
                #Makes the current node's value as the minimum value from the right-subtree.
                #Then, implements the function to remove that last value. 
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

def main():
    num = int(input("Enter Root Value:"))
    bst = BinarySearchTree(num)

    while True:
        op = input("Type 'insert' , 'delete' or 'search' for operations.")

        if op == "insert":
            num = int(input("Integer:"))
            bst.insert_node(num)
            bst.printTree()
        elif op == "search":
            num = int(input("Integer:"))
            print(bst.find_node(num,[]))
        elif op == "delete":
            num = int(input("Integer:"))
            bst.remove_node(num,None)
            bst.printTree()

main()

      

