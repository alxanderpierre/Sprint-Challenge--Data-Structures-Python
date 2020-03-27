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
            if self.current != None: # head
        # set the item to  the current value
                self.current.value = item
                self.current = self.current.value

            else:
                #if self.current.next is None: # tail
                    #self.storage.tail.value = item





    def get(self):


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
