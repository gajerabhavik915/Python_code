print('Now we will try to create LinkedList')

class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        created_node = node(value)
        self.head = node
        self.tail = node
        self.len = 1

    def printing_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return True

    def Append(self, value):
        created_node = node(value)
        if self.head is None:
            self.head = created_node
            self.tail = created_node
            self.len = 1

        else:
