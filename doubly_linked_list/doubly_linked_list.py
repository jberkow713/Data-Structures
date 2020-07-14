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
        

     


    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node =ListNode(value, None, None)
        self.length +=1

        if self.head is None and self.tail is None:

            self.head = new_node
            self.tail = new_node

        else:
            self.length +=1    
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
        
        self.length -=1
        removed_head = self.head.value
        self.delete(self.head)
        return removed_head 

            
        

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        tail_node =ListNode(value, None, None)
        self.length +=1

        if self.head is None and self.tail is None:

            self.head = tail_node
            self.tail = tail_node

        else:

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
        
        self.length -=1
        removed_tail = self.tail
        self.delete(self.tail)
        return removed_tail   


        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return 
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
        self.length -=1
        if self.head == self.tail:
            self.head = None
            self.tail = None 

        # node is the head node, handle head pointer correctly

        elif self.head == node:
            self.head = node.next
            node.delete()

        # node is tail node, make sure tail handled correctly
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()    
        # node just some node in the list
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass