#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Note that this Pre-class Work is estimated to take **26 minutes**.
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[43]:


NAME = "MUHAMMAD ABDURREHMAN ASIF"
COLLABORATORS = ""


# ---

# # CS110 Pre-class Work - Writing algorithms in Python--part I
# 
# ## Question 1 [time estimate: 10 minutes]
# 
# Palindromes are a sequence of characters (words, phrases, numbers) that can be read the same both from left to right and from right to left. Examples of palindromes include the word 'madam' and the number 12321.
# 
# 1. Explain how you would use an iterative approach, step by step, to check whether a word is a palindrome.
# 2. Explain also how you would approach this problem using a recursive solution.
# 
# You can use palindromic and non-palindromic words to assist your explanation. 

# 1.  Iteratively, solving this problem is very intuitive. First we have to define certain local variables. These will be 
#     necessary since the iteration will require a range so it runs til a point as well as defines one of the iterative
#     outcomes such that we get our required result upon the code working appropriately. Next, we will compare the first and
#     last letters of the input iteratively, keeping the outcome constant if the comparison is okay and breaking the loop
#     if the comparison shows discrepancy
#     
#     So, step by step:
#     Define the function
#     Define the local variables for the middle letter and the output being True
#     Write a for loop that runs through the range until the midpoint we set up
#     Compare the first and last letter using the for loop, keep it running if both letters are the same
#     Break once they are not the same, or until midpoint is reached
#     
# 
# 
# 2.  From a recursive point of view, a different approach has to be used. First of all, we need to set up the base case.
#     Once set up, we can then take the approach of closing down on the spring from it's first and last elements. The only
#     implications we need to be careful are, 1- the recursion will continue til only 1 or 0 elements are left, or 2, the
#     recursion must occur until one of the pairs of elements do not match.
#     
#     So, step by step:
#     Check whether word has less than 2 letters, if not
#     Check whether first and last letters are the same, 
#     recursively repeat the function for the next set of first and last letters
#     return true if base case is achieved, false if otherwise

# ## Question 2 [time estimate: 3 minutes]
# 
# How would you prevent your recursive solution from running forever? In other words, what is the base case of your recursive approach?

# The base case I set up is the word having less than 2 letters remaining. Since our code is convergent in nature, we will observe the letters being compared and the midpoint drawing closer. If it is an even-lettered word, we will see 0 letters remain and base case being achieved, if it is odd we will see only 1 letter remain and base case being achieved. Thus, if all other letters are palindromic, the final letter does not change anything.

# ## Question 3 [time estimate: 3 minutes]
# 
# Is there a base case in an iterative approach? Why or why not?

# Since iteration is repetitive in nature and not selective, there has to be certain inputs given to the program to ensure it does not keep running forever. This is not a base case, however, since the function terminates once the loop continuation condition fails; more simply, the loop completes the job it was given to do within the parameters identified. 

# ## Question 4 [time estimate: 10 minutes]
# 
# Given the algorithmic strategies you described in question 1, you will now implement these in Python code. Write a function for the iterative approach (using either a `for` or a `while` loop) and another function for the recursive approach. Both functions should return `True` if the provided word is a palindrome, and `False` if the word is not. 
# 
# Validate the correctness of your code by providing examples of words that can be used as test cases. Be prepared to paste your functions and Palindrome words you searched into a Minerva workbook during class.

# In[44]:


def is_palindrome_iterative(word):
    """
    This function identifies whether a word is a palindrome iteratively.

    Parameters
    ----------
    word : str
        Word we wish to check
    
    Returns
    -------
    bool
        True if input is a palindrome, False otherwise
        
    """
  
    #initiating 2 of the variables we will call up in the function
    middle = len(word)//2
    output = True
    
    for i in range(0,middle):  #for loop to run iteration, range is defined in a convergent function uptil the middle element
      
        first = word[i]             #the first variable we will compare
        last = word[len(word)-i-1]  #initiating the second variable, and adding in 'i' to run iteration until break
        if first!=last:             #condition which shows word is not palindrome
            output =False
            break
            
    return output    
    raise NotImplementedError()
    
is_palindrome_iterative('abba')


# In[46]:


def is_palindrome_recursive(word):
    """
    This function identifies whether a word is a palindrome recursively.

    Parameters
    ----------
    word : abba
        Word we wish to check
    
    Returns
    -------
    boolean
        True if input is a palindrome, False otherwise
        
    """
    #YOUR CODE HERE
   
    if len(word) < 2:   #if only one letter, then obviously palindrome
        return True
    if word[0] != word[-1]:  #for it to be a palindrome, the first and last letter need to be the same
        return False         
    #print(word[0])   uncomment to take a deeper look into the recursion occuring
    #print(word[-1])
    return is_palindrome_recursive(word[1:-1])  #this is the recursive part that takes the string as a variable and compares it
                                                #to the corresponding input and as long as we do not reach "false" it continues running
   
    raise NotImplementedError()
    

is_palindrome_recursive("settes")


# In[ ]:




