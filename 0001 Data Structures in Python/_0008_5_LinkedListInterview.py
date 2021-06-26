from random import randint

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next
            
    def __str__(self):
        values = [str(i) for i in self]
        return "-->".join(values)
    
    def __len__(self):
        values = [str(i) for i in self]
        return len(values)
        
        
    def insert_end(self,value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next 
            
    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert_end(randint(min_value,max_value))
        return
        
        