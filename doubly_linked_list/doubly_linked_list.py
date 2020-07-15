"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    # self.length =1 if node exists, otherwise 0
    def __len__(self):
        return self.length    
        

     


    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node =ListNode(value)
        self.length +=1   
        #Again, you are adding length regardless
        # of where the procedure takes place, 
        # so the length function takes place
        # outside the if, else statement
        if self.head is None and self.tail is None:

            self.head = new_node
            self.tail = new_node

        else:
            # setting the newly created nodes next
            # value to the previous head, 
            # setting the previous heads previous value 
            # to the new node, thus creating 2
            # new reference points to the new node
            # as the new head   
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
  

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None 
        #set variable = to self.head.value...VALUE only
        # use delete function created below to remove the
        # specific node from the head of the Doubly Linked
        # List, and then return the removed head VALUE
        
        removed_head = self.head.value
        self.delete(self.head)
        
        return removed_head 

            
        

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #using listnode class to declare a new variable
        # by doing so within the doubly linked list 
        #class, you can use the attributes of the
        # ListNode class

        # add 1 outside the if else statement because you 
        # are adding 1 to length regardless of which situation
        # you add to the tail,
        #for subtraction, it is different procedure
        tail_node =ListNode(value, None, None)
        self.length +=1

        if self.head is None and self.tail is None:

            self.head = tail_node
            self.tail = tail_node

        else:
         # setting the new tail_nodes previous point
         # equal to the previous tail, and 
         # setting the old tails next point equal
         # to the new tail node, thus creating 2
         # new reference points to the new tail       
            tail_node.prev = self.tail 
            self.tail.next = tail_node
            self.tail = tail_node




            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None 
        
        # set variable = to tail value
        # use the delete function you created below
        # to delete the tail
        # and then return the VALUE of removed tail, 
        # ONLY the VALUE is being returned here, 
        #REPRESENTED by removed_tail
        removed_tail = self.tail.value
        self.delete(self.tail)
        
        return removed_tail   


        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return 
        # use the delete function to delete this
        # node, and then use the add to head function
        # to move this to the head
        # you are moving the nodes value, 
        # and not the node itself, because
        # add to head has a value attribute in its
        #method, and not a node value, so you are
        # sort of transferring the essence from the
        #node attribute in this method, to the 
        # add to head attribute
        moved_value = node.value
        self.delete(node)
        self.add_to_head(moved_value)





        



        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        #use the delete function to delete the nodes value
        # then combine it with the add to tail 
        # function to add it to the end of the chain
        #same thing , getting a value , deleting the node
        # using delete function which has node attribute,
        # moving to tail , through add to tail, which has
        # value attribute, node --->> value
        end_value = node.value
        self.delete(node)
        self.add_to_tail(end_value)
        
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #linked list completely empty: do nothing
        if self.head is None and self.tail is None:
            return
        # list is only one node: 
        # if only one node, meaning tail = head, you 
        # declare the one node equal to the head
        # and the tail, set both = to None, and 
        # delete the length by 1
        self.length -=1
        if self.head == self.tail:
            self.head = None
            self.tail = None 

        # node is the head node, handle head pointer correctly
        # so here, you are pushing self head a step forward
        # and then sending it back to where it was
        # but declaring where it was as None, thereby
        # essentially deleting the node itself
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            

        # here you are declaring that the tail is equal
        # to the previous node, and then sending the previous
        # node back to where the tail was, and declaring it
        # None, thereby deleting the tail
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        #Here you are severing the connection to the node
        # from both directions, by saying the previous nodes
        # next direction is equal to this nodes next,
        # and by saying the next nodes previous direction
        # is equal to this nodes previous, essentially
        # pointing the node in front of the current node
        # towards the node behind it, and pointing the node behind
        # this node, to the node in front of it...trippy    
        else:
            node.prev.next = node.next
            node.next.prev = node.prev   
        # node just some node in the list
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value    
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value