
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