NO_OF_CHARS = 256  
    
""" function to check whether characters of a string 
   can form a palindrome """
def canFormPalindrome(string): 
      
    # Create a count array and initialize all  
    # values as 0 
    count = [0 for i in range(NO_OF_CHARS)] 
    
    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in string: 
        count[ord(i)] += 1
    
    # Count odd occurring characters 
    odd = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] & 1): 
            odd += 1
   
        if (odd > 1): 
            return False
    
    # Return true if odd count is 0 or 1,  
    return True

a=input("Enter a word")
if(canFormPalindrome(a)): 
    print("Yes" )
else: 
    print("No")

