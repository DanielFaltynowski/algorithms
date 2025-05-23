class Stack:
    def __init__(self, capacity = 64):
        self.__stack = [None] * capacity
        self.__top = 0
        self.__capacity = capacity

    def get(self):
        if self.is_empty():
            print('The stack is empty!')
        else:
            return self.__stack[self.__top - 1]

    def add(self, elem):
        if self.is_full():
            print('The stack is full!')
        else:
            self.__stack[self.__top] = elem
            self.__top = self.__top + 1

    def remove(self):
        if self.is_empty():
            print('The stack is empty!')
        else:
            self.__top = self.__top - 1
            self.__stack[self.__top] = None
    
    def is_empty(self):
        return self.__top == 0
    
    def is_full(self):
        return self.__top == self.__capacity
    
    def size(self):
        return self.__top
    
    def capacity(self):
        return self.__capacity

    def __str__(self):
        response = '\n'
        if not self.is_empty():
            counter = self.__top - 1
            while counter >= 0:
                response = response + f'[{counter}] {self.__stack[counter]}\n'
                counter = counter - 1
            return response
        else:
            response = response + 'The stack is empty!\n'


class Queue:
    def __init__(self, capacity = 64):
        self.__queue = [None] * capacity
        self.__front = 0
        self.__back= 0
        self.__capacity = capacity
    
    def get(self):
        if self.is_empty():
            print('The queue is empty!')
        else:
            return self.__queue[self.__front]
    
    def add(self, elem):
        if self.is_full():
            print('The queue is full!')
        else:
            self.__queue[self.__back] = elem
            self.__back = (self.__back + 1) % self.__capacity
    
    def remove(self):
        if self.is_empty():
            print('The queue is empty!')
        else:
            self.__queue[self.__front] = None
            self.__front = (self.__front + 1) % len(self.__queue)

    def is_empty(self):
        return self.__front == self.__back and self.__queue[self.__front] is None
    
    def is_full(self):
        return self.__front == self.__back and self.__queue[self.__front] is not None
    
    def size(self):
        if self.__queue[self.__front] is not None and self.__front == self.__back:
            return self.__capacity
        else:
            return (self.__back - self.__front) % self.__capacity
    
    def capacity(self):
        return self.__capacity
    
    def __str__(self):
        response = '\n'
        if not self.is_empty():
            i = self.__front
            j = 0
            if not self.is_full():
                while not self.__queue[i] == None:
                    response = response + f'[{j}] {self.__queue[i]}\n'
                    i = (i + 1) % len(self.__queue)
                    j = j + 1
            else:
                while j < len(self.__queue):
                    response = response + f'[{j}] {self.__queue[i]}\n'
                    i = (i + 1) % len(self.__queue)
                    j = j + 1
        return response


class LinkedNode:
    def __init__(self, elem, next = None):
        self.__value = elem 
        self.__next = next
    
    def get_value(self):
        return self.__value
    
    def get_next(self):
        return self.__next
    
    def set_value(self, elem):
        self.__value = elem
    
    def set_next(self, next):
        self.__next = next
    
    def __str__(self):
        return str(self.__value)


class LinkedList:
    def __init__(self):
        self.__head = None
    
    def get(self):
        return self.__head.get_value()
    
    def add(self, elem):
        self.__head = LinkedNode(elem, self.__head)
    
    def remove(self):
        self.__head = self.__head.get_next()
    
    def is_empty(self):
        return self.__head is None
    
    def size(self):
        counter = 0
        current = self.__head
        while current is not None:
            counter = counter + 1
            current = current.get_next()
        return counter
    
    def __str__(self):
        response = '\n'
        if self.__head is None:
            response = response + 'The linked list is empty!\n'
        else:
            current = self.__head
            while current.get_next() is not None:
                response = response + f'({current.get_value()}) -> '
                current = current.get_next()
            response = response + f'({current.get_value()})\n'
        return response




if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
    print(ll.size())