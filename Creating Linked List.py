print('Now we will try to create LinkedList')

class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        created_node = node(value)
        self.head = created_node
        self.tail = created_node
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
            self.tail.next = created_node
            self.tail = created_node
            self.len +=1
        return True


    def pop(self):
        if self.len == 0:
            return False
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.len -= 1

        return True

    def prepend(self, value):
        created_node = node(value)
        if self.head is None:
            self.head = created_node
            self.tail = created_node
        else:
            created_node.next = self.head
            self.head = created_node
        self.len += 1

    def pop_first(self):
        if self.head is None:
            return False
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.len -= 1

    def Get(self, index):
        temp = self.head
        if index <= 0 and index > self.len:
            return False
        else:
            for a in range(index-1):
                temp = temp.next
            return temp

    def set(self, index, value):
        temp = self.head
        if index <= 0 and index > self.len:
            return False
        else:
            temp = self.Get(index)
            temp.value = value
        return True

    def insert(self,index, value):
        created_node = node(value)
        temp = self.head
        if index < 0 and index > self.len:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.len:
            return self.Append(value)
        else:
            temp = self.Get(index-1)
            temp.next = created_node
            created_node.next = temp.next


    def reverse(self):
        if self.head.next is None:
            return True
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            after = temp.next
            for a in range(self.len):
                after = temp.next
                temp.next = before
                before = temp
                temp = after









linklist = LinkedList(2)
print(linklist.printing_list())
(linklist.Append(3))
(linklist.Append(4))
(linklist.Append(5))
print(linklist.printing_list())
(linklist.prepend(1))
(linklist.insert(5,6))
print(linklist.printing_list())
linklist.reverse()
print(linklist.printing_list())