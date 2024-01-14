#!/usr/bin/env python
# coding: utf-8

# # 1a

# In[1]:


import random

def process_string(user_input):
    if len(user_input) < 2:
        return "Enter a string with at least 2 characters."
    
    remove_chars = random.sample(range(len(user_input)), 2)
    
    output_word = [user_input[i] for i in range(len(user_input)) if i not in remove_chars]
    
    return ''.join(reversed(output_word))

print(process_string(input(("Enter the string: "))))


# # 1b

# In[2]:


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Sum: {add(num1, num2)}")
print(f"Difference: {subtract(num1, num2)}")
print(f"Product: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")
print("a")


# # 2

# In[3]:


def replace_function(text, word, replacement):
    return text.lower().replace(word.lower(), replacement)

input_sentence = input("Enter a sentence: ")

output_sentence = replace_function(input_sentence, "python", 'pythons')

print("Output sentence:", output_sentence)


# # 3

# In[4]:


def get_letter_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'

class_score = float(input("Enter the class score: "))
grade = get_letter_grade(class_score)

print(f"Grade: {grade}")


# In[ ]:




