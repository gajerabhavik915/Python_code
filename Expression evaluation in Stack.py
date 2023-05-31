class stack:
    def __init__(self, stack_list):
        self.stack_list = []

    def print(self):
        print(self.stack_list)

    def append(self, val):
        self.stack_list.append(val)

    def pop(self):
        self.stack_list.pop()


    def pop1(self):
        a = self.stack_list.pop()
        return a

    def length(self):
        print(len(self.stack_list))

    def take_input(self, Q_list):
        l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for i in Q_list:
            if i in l:
                self.append(int(i))
            else:
                top = self.pop1()
                sec_top = self.pop1()
                if i is '*':
                    append = sec_top*top
                    self.append(append)
                elif i is '+':
                    sum = sec_top+top
                    self.append(sum)
                elif i is '/':
                    div = sec_top//top
                    self.append(div)
                elif i is '-':
                    sub = sec_top-top
                    self.append(sub)
                else:
                    continue




    #
    # def multiplication(self, top, sec_top):
    #     self.append(top*sec_top)









stack = stack([])
stack.print()
stack.append(1)
stack.print()
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.length()
stack.print()
stack.pop()
stack.print()

