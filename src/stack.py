class stack : 
    def __init__(self): 
        self.items=[]

    # def push (self,value): 
    #     self.items.append(value)
    
    def push(self, *values):
        for value in values:
            self.items.append(value)
    
    def pop (self):
        poped_item= self.items.pop()
        return poped_item 
    
    def peek (self) : 
        return self.items[-1] 
    
    def get_current (self):
        return self.items
    
    def is_empty (self):
        return len(self.items) == 0
    
    
    def get_stack_size(self):
        return len(self.items)  
    

    def contains(self, value):
        return value in self.items 
    
    # def cont (self , value) : 
    #     return self.items.__contains__(value)

