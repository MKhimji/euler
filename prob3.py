"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


#  Start basic to learn basic python better
#  Write function to test if a number is prime

def is_prime(n):
        for x in range(2,n):
                if n % x == 0:
                        return False
        return True


# Practise functions

# Continually divide n by 2 until 
# the remainder is not zero
# Then do same process with 3, 4 etc


def prf(n):
        i=2
        while n % i == 0:        
                yield n/i       
                n=n/i
                i+=1

def prfm(n):
        i=2
        while True:
                try:
                        n % i == 0        
                        yield n/i       
                        n=n/i
                except:
                        n % i != 0
                        i+=1
                        yield n/i
                        n=n/i     

               

# This function takes a number and 
# continually divides it by 2 
# until there is a remainder
# At which point it incremens the 2
#  by 1 and tries dividing n by 3 until
# .. function is not complete yet         
        
def prf2(n):
        i = 2
        while True:
                if n % i == 0:
                        yield n/i
                        n=n/i       
                else:
                        i+=1
                        continue

        

      

        # if a % 2 != 0:

        #         i+= 1        
                



        
        





       

                

        
  
    
                
     
