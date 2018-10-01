class Element():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value
