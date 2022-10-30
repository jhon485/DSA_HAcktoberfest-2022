class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None  
class Stack:
    def __init__(self):
        self.head = None
        self.counter=0
 
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
 
    def push(self, data):
        self.counter+=1
        if self.head == None:
            self.head = Node(data)
 
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
      
    def pop(self):
        self.counter-=1
        if self.isempty():
            return None
 
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    def length(self):
        if self.isempty():
            return None
        else:
            return self.counter  
    
            
 
if __name__ == "__main__":
  MyStack = Stack()
  print(MyStack.isempty()) 
  MyStack.push(11)
  MyStack.push(22)
  MyStack.push(33)
  MyStack.push(44)
  MyStack.push(55)
  MyStack.push(66)
  MyStack.push(77)
  MyStack.push(88)
  print(MyStack.length())
  MyStack.pop()
  MyStack.pop()
  MyStack.pop()
  MyStack.pop()
  MyStack.push(99)
  MyStack.push(110)
  while MyStack.isempty()==False:
      MyStack.pop()
print(MyStack.length())
  
    
  

 
  