"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # compare input value with value of node
        # go left if value is smaller than value of node
        # otherwise value >= Nodes value, and go right
        
        # value is just a number, when you insert it,
        # you insert it in the BSTNode class, and then
        # it becomes an actual Node, with a value
        # if no node to compare input value to,
        # then wrap value in BSTNode and put it there

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)    

        if value >= self.value:

            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)
  
        

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        
       
        if self.value <= target:
            if self.right is None:
                return False
            # otherwise use code above and run it again, 
            # treating self.right as self, and checking if 
            # that value <= or > target    
            return self.right.contains(target)  
        
        if self.value > target:
            if self.left is None:
                return False 
            #So you are writing function initially,
            # and  as you are
            # going along you are implementing it, 
            # this is recursion
            
    
    # if at any point the left or right branch = None,
    # the actual function will RETURN false, and 
    # essentially end...until then, it will scroll through
    # search every possible branch until it finds true,
    # or until it finds NONE...so it will either return 
    # TRUE, when it finds the match, or NONE when it gets 
    # to the end of the branch and finds nothing 
            #
            return self.left.contains(target)
       #basically, created 3 if statements, which make up the function
       # then as youre writing the function, you use the same function
       # on self.right, and self.left, treating them essentially as self,
       # causing the function to loop back outside of the loop in which 
       #self.right and self.left were referenced in
       
        

              
     
    
    # Return the maximum value found in the tree
    def get_max(self):


        # so this below is the function,
        # if at any point self.right returns None, then self.value
        # is the maximum value of previous node self
        
        if self.right is None:
            return self.value

        # so what if the next value is not None? What will the function do?
        # logically, it seems as if it has no choice but to then check
        # that next positions self.right to see if that is None
        #     

        # so apply this function now, within the same function
        return self.right.get_max()
              
        #not using recursion here, just walking down
        # the line until reach self.right is None
        # and printing previous value


        


        
    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # so defined the function above,
        # called function on self.value

        if self.left:
            self.left.for_each(fn)
        
        
        if self.right:
            self.right.for_each(fn)

        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go to each node, print node

            
        # so defined the function above,
        # called function on self.value

        if self.left:
            self.left.in_order_print(node) 
        
        print(self.value)
        

        if self.right:
            self.right.in_order_print(node)

        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        # BFT: FIFO 
        # we'll use a queue to facilitate the ordering 
        queue = deque()
        queue.append(self)
        
        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
                
            print(current.value)       
          
   
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack)>0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            print(current.value)   

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
