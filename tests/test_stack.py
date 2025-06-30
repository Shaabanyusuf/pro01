from src.stack import stack 
import pytest 



class TestStack: 

    def test_push(self):
         stc = stack()
         stc.push(10)
         stc.push(11)
         stc.push(12)
         stc.push(13)
         assert stc.is_empty() == False 
               
    def test_pop(self):
         stc = stack()
         stc.push(10)
         stc.push(11)
         stc.push(12)
         stc.push(100)

         assert stc.pop() == 100

    def test_peek (self):
        
         stc = stack()
         stc.push(10)
         stc.push(11)
         stc.push(12)
         stc.push(100)

         assert stc.peek() == 100

    def test_is_empty(self):
         stc = stack()
         assert stc.is_empty() == True 

    def test_contains(self):
         stc = stack()
         stc.push(100)
         assert stc.contains(1000) == False 
         assert stc.contains(100) == True 

    def test_size_current(self):
         stc=stack()
         stc.push(10,11,12,13)
         assert stc.get_current() == [10,11,12,13] 
         assert stc.get_stack_size() == 4


    



    


    
         
     
     

    
    


