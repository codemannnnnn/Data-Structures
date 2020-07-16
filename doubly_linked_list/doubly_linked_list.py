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

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    # init with next and prev, this will become with new head,
    # new node pointing to it
    #

    def add_to_head(self, value):
        # create a ListNode with the passed in value
        new_node = ListNode(value)

       #If there is NOT a head
        if self.head is None and self.tail is None:
            # set the head and tail to new_node
            self.head = new_node
            self.tail = new_node
            # update length +1
            self.length += 1
        else:
            # 1. reassign head field of the DoublyLinkedList Class
            old_head = self.head
            # 2. new_node or current head's next value needs to
            # old head
            self.head = new_node
            self.head.next = old_head
            # 3. old head prev need to point to new head or new_node
            old_head.prev = self.head
            # 4 update length +1
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        if self.head is None and self.tail is None:
            return
        elif self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value

        else:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            old_tail = self.tail
            self.tail = new_node
            self.tail.prev = old_tail
            old_tail.next = self.tail
            self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        old_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        else:

            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return old_tail.value



    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:
            return None
        elif self.head is self.tail:
            return
        else:
            node.prev = None
            node.next = self.head
            self.head = node


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return None

        elif self.tail == node:
            return

        elif self.head == node:
            self.delete(node)
            self.add_to_tail(node.value)


        elif self.length > 1:
            node.next = None
            node.prev = self.tail
            self.tail = node



    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1



    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head:
            current = self.head
            max = current.value
            while current.next:
                current = current.next
                if current.value > max:
                    max = current.value
            return max
        else:
            return None
