from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.len = 0

    def append(self, item):
        # first have to check if the length of the list is = to the capacity

        if self.len == self.capacity:
        # if it is we have to override the oldest item

            if self.current.next is not None:
                self.current.value = item
                self.current = self.current.next

            elif self.current.next is None:
                self.storage.tail.value = item
                self.current = self.storage.head


        # now if its not at capacity
        else:
            if self.len < self.capacity:
                self.storage.add_to_tail(item)
                self.current = self.storage.head
                self.len += 1

        # return
    def get(self):
        list_buffer_contents = []
        # check to see if there is nothing in the list to get
        if self.len is None:
            return []
        # now if there is something in the list to get
        else:
            current = self.storage.head
            while current:
                #append the current value to the list
                list_buffer_contents.append(current.value)
                #set the next to the current
                current = current.next

        return list_buffer_contents




# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
