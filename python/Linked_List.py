class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """To append an element at the end of the Linked List"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        first_element = self.head
        next_element = first_element
        if position < 1:
            return None
        for i in range(1, position):
            next_element = next_element.next
            if next_element is None:
                return None
        return next_element

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        elem_at_pos = self.get_position(position)
        new_element.next = elem_at_pos
        if position == 1:
            self.head = new_element
        elif position > 1:
            self.get_position(position-1).next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        i = 1
        while self.get_position(i) is not None:
            elem_at_pos = self.get_position(i)
            if elem_at_pos is not None:
                if elem_at_pos.value == value:
                    if i == 1:
                        self.head = elem_at_pos.next
                        elem_at_pos.next = None
                    elif i > 1:
                        self.get_position(i-1).next = elem_at_pos.next
                        elem_at_pos.next = None
            i += 1
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
