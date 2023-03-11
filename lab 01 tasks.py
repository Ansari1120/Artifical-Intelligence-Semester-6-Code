#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3. Assuming (name = “John Smith”), what does name[1] return?

#Answer:

name = "John Smith" 
print(name[1])


# In[2]:


#4. What about name[-2]?

#Answer:

name = "John Smith" 
print(name[-2])


# In[3]:


#5. What about name[1:-1]?

#Answer:

name = "John Smith" 
print(name[1:-1])


# In[4]:


#6. How to get the length of name?

#Answer:

name = "John Smith"
str_len = len(name)
print(str_len)


# In[7]:


#7. What is the result of f“{2+2}+{10%3}”?

#Answer:

f = (2+2)+(10%3)
print(f)


# In[14]:


#9. Write a program to get two number from user and print sum, difference, 
#module, division and multiplication of the numbers, also show the type of the enter data.

#Answer:

valueOne = input('Enter First Number : ')
valueTwo = input('Enter Second Number : ')

add = (int(valueOne) + int(valueTwo))
sub = (int(valueOne) - int(valueTwo))
div = (int(valueOne) / int(valueTwo))
mul = (int(valueOne) * int(valueTwo))

data = type(valueOne)
data2 = type(valueTwo)
print("Addition : ",add , data,data2)
print("Substraction : ",sub)
print("Division : ",div)
print("Multiplication : ",mul)


# In[ ]:




