class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        current_node = self.head
        previous = None
        # new = current_node.next_node
        # current_node.next_node = None

        while current_node:
            if current_node.next_node == None:
              # if next node is none end of list set current node to head
                self.head = current_node
            # save our next node
            the_next_node = current_node.next_node
            # assign new next node to current node
            current_node.next_node = previous
            # assign current to previous node
            previous = current_node
            # current node is now the next node
            current_node = the_next_node

        # while new is not None:
        #     previous = current_node
        #     current_node = new
        #     new = current_node.next_node
        #     current_node.next_node = previous

        # while current_node is not None:
        #     # if current.next_node == None:
        #     #     self.head = current

        #     next_node = current_node.get_next()
        #     # current_node.next_node = previous
        #     current_node.set_next(previous)
        #     previous = current_node
        #     # previous = current
        #     current_node = next_node

        # def reverse(self):
        #     cur = self
        #     new = cur.next

        #     cur.next = None
        #     while new != None:

        #     prev = cur
        #     cur = new
        #     new = cur.next
        #     cur.next = prev

        #     return cur
