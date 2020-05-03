#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# In[46]:


def my_reduce(function,sequence):
    
    '''
    Implementing my own reduce function my_reduce() which works as python's reduce()
    '''
    #Allocating the first value of the given list in a variable 'firstItem'
    
    firstItem = sequence[0]
    
#     Iterating over the given list from the second element till the last element and applying the function
    
    for item in sequence[1:]:
        firstItem = function(firstItem,item)
        
    #returning the result that is stores in the variable firstItem
    
    return firstItem

#Printing Sum of elements in a list using my_reduce function

print("Sum of elements in a given list :"+str(my_reduce(lambda a,b:a+b,[1,2,3,4])))

#Test function for adding all elements in a list    

def my_sum(a,b):
    return a+b

# test case for my_sum function
print("Sum of elements in a given list :"+str(my_reduce(my_sum,[4,5,6])))

#Printing the maximum value among the given values
print("maximum value among the given values :"+str(my_reduce(lambda a,b: a if (a > b) else b, [10,20,30])))

1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()
# In[48]:


def my_filter(function,sequence):
    
    '''
    Implementing my own reduce function my_filter() which works as python's filter()
    '''
    
     # Creating an empty list and store it in a variable result
    result=[]
    
    #Iterating over the given list 
    
    for item in sequence:
        #conditonal check for the item
        if function(item):
            result.append(item)
        #returning the result
    return result

# Printing list of even numbers in a given range 
print(my_filter(lambda a: a%2==0,range(2,11)))


# 2. Implement List comprehensions to produce the following lists.
# 
# Write List comprehensions to produce the following Lists
# 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[64]:


list1 = ['x','y','z']
[i*j for i in list1 for j in range(1,5)]


# In[66]:


[i*j for j in range(1,5) for i in list1]


# In[69]:


[[i+j] for i in [0,1,2] for j in [2,3,4]]


# In[73]:


[[i+j for i in range(4)] for j in range(2,6)]


# In[75]:


[(j,i) for i in range(1,4) for j in range(1,4) ]

