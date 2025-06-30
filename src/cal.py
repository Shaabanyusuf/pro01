


def add (a, b ):
      return (a+b)
   
def sub (a, b):
    return a-b

def mult (a,b):
    return a*b

def power (a, b):
    return a**b


def div (a, b):

      # if b != 0:
      #     return a/b
      # else:
      #     print("pls enter corret value not zero or char ") 
      

    res=0
    try: 
       res= a/b 
       
    except ZeroDivisionError : 
        print("can not div by zero ")
    except Exception as ex1 :
        print(ex1)
    return(res)

def abs (x):
    if x > 0 :
        return x 
    else:
        return x * -1
    
    


div (5,"g")




    



