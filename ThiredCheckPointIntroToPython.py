#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Write a Python program to multiplies all the items in a list.
def Multp(list):
    result = 1
    for x in range(len(list)): 
        result  = result* list[x]
    
    return result
Multp([2, 3, 6])


# In[7]:


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def lastelement(n): return n[-1]

def SortTuplesList(list):
  return sorted(list, key=lastelement)

print(SortTuplesList([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[23]:


# Write a Python program to combine two dictionary adding values for common keys.
def Combine (d1, d2):
    d3 = dict(d1)
    d3.update(d2) 
    for i, j in d1.items(): 
        for x, y in d2.items():
            if i == x:
                d3[i]=(j+y)
    
    return d3

Combine( {'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400}) 


# In[24]:


# Write a program to sort a tuple by its float element.
def Sort(list):  
    return(sorted(list, key = lambda x: float(x[1]), reverse = True)) 
Sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])


# In[ ]:




