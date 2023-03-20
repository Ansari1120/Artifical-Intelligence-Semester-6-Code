#!/usr/bin/env python
# coding: utf-8

# **Conditional Statements**
# 

# In[1]:


num = 5
if num > 0:
    print(num, "is a positive number.")
print("This statement is true.")


# In[2]:


a = 33
b = 200

if b > a:
  print("b is greater than a")


# In[3]:



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# In[4]:


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# In[5]:


num = 8
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# In[6]:


age = int(input("Age of the dog: "))
print()
if age < 0:
    print("This cannot be true!")
elif age == 0:
    print("This corresponds to 0 human years!")
elif age == 1:
    print("Roughly 14 years!")
elif age == 2:
    print("Approximately 22 years!")
else:
    human = 22 + (age -2) * 5
    print("Corresponds to  " + str(human) + " human years!")


# In[7]:


x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y and x > z:
    maximum = x
elif y > x and y > z:
    maximum = y
else:
    maximum = z

print("The maximal value is: " + str(maximum))


# In[ ]:


height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi = weight / height ** 2
print(bmi)
if bmi < 15:
    print("Very severely underweight")
elif bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal (healthy weight)")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I (Moderately obese)")
elif bmi < 40:
    print("Obese Class II (Severely obese)")
else:
    print("Obese Class III (Very severely obese)")


# **Loops in Python**

# In[7]:


numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
  
# variable to store the square of the number  
square = 0  
  
# Creating an empty list  
squares = []  
  
# Creating a for loop  
for value in numbers:  
    square = value ** 2  
    squares.append(square)  
print("The list of squares is", squares)  


# In[1]:


string = "Python Loop"  
  
# Initiating a loop  
for s in  string:  
    # giving a condition in if block  
    if s == "o":  
        print("If block")  
    # if condition is not satisfied then else block will be executed  
    else:  
        print(s)  


# In[2]:


tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")  
  
# iterating over tuple_ using range() function  
for iterator in range(len(tuple_)):  
    print(tuple_[iterator].upper()) 


# In[3]:



counter = 0  
# Initiating the loop  
while counter < 10: # giving the condition  
    counter = counter + 3  
    print("Python Loops")


# In[4]:



counter = 0  
  
# Iterating through the while loop  
while (counter < 10):      
    counter = counter + 3  
    print("Python Loops") # Executed untile condition is met  
# Once the condition of while loop gives False this statement will be executed  
else:  
    print("Code block inside the else statement")  


# In[6]:


for string in "Python Loops":  
    if string == "o" or string == "p" or string == "t":  
         continue  
    print('Current Letter:', string)  


# In[5]:


for string in "Python Loops":  
    if string == 'L':  
         break  
    print('Current Letter: ', string)  


# In[ ]:





# In[ ]:





# In[ ]:




