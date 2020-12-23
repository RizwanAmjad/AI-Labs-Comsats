class Stack:

    def __init__(self):
        self.stk = list()
        self.count = 0

    def push(self, value):
        self.stk.append(value)
        self.count += 1

    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.stk.pop()
        else:
            return None

    def to_string(self):
        return str(self.stk)


class Queue:

    def __init__(self):
        self.back = list()
        self.count = 0

    def enqueue(self, value):
        self.back.append(value)
        self.count += 1

    def dequeue(self):
        if self.count > 0:
            self.count -= 1
            return self.back.pop(0)
        else:
            return None

    def to_string(self):
        return str(self.back)


class Priority_Queue:

    def __init__(self, reverse_priority=False):
        self.back = list()
        self.count = 0
        self.reverse_priority = reverse_priority

    def enqueue(self, value):
        self.back.append(value)
        self.count += 1

    def dequeue(self):
        if self.count > 0:
            self.count -= 1
            if self.reverse_priority:
                return self.back.remove(max(self.back))
            else:
                return self.back.remove(min(self.back))
        else:
            return None

    def to_string(self):
        return str(self.back)


def main():
    my_stack = Stack()
    my_stack.push(9)
    print(my_stack.to_string())

    q = Priority_Queue(True)
    q.enqueue(90)
    q.enqueue(10)
    q.enqueue(9)
    q.enqueue(100)
    print(q.to_string())
    q.dequeue()
    print(q.to_string())
    q.dequeue()
    print(q.to_string())


if __name__ == "__main__":
    main()
