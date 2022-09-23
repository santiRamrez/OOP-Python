class Stack:
    def __init__(self):
        self.__stk = [] # private property
        self.stk = [] # public property

    def getStk(self): #getter
        return self.__stk

stack = Stack()
print(stack.__stk) # 'Stack' object has no attribute '__stk'
