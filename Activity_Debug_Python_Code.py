#!/usr/bin/env python
# coding: utf-8

# # Activity: Debug Python Code

# ## Introduction
# 
# One of the biggest challenges faced by analysts is ensuring that automated processes run smoothly. Debugging is an important practice that security analysts incorporate in their work to identify errors in code and resolve them so that the code achieves the desired outcome. 
# 
# Through a series of tasks in this lab, you'll develop and apply your debugging skills in Python.

# <details><summary><h2>Tips for completing this lab</h2></summary>
# 
# As you navigate this lab, keep the following tips in mind:
# 
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task. 
# - To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook. 
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook. 
# </details>

# ## Scenario
# 
# In your work as a security analyst, you need to apply debugging strategies to ensure your code works properly.
# 
# Throughout this lab, you'll work with code that is similar to what you've written before, but now it has some errors that need to be fixed. You'll need to read code cells, run them, identify the errors, and adjust the code to resolve the errors.

# ## Task 1
# 
# The following code cell contains a syntax error. In this task, you'll run the code, identify why the error is occuring, and modify the code to resolve it. (To ensure that it has been resolved, run the code again to check if it now functions properly.)

# In[2]:


# For loop that iterates over a range of numbers
# and displays a message each iteration

for i in range(10):
    print("Connection cannot be established")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# The header of a `for` loop in Python requires specific punctuation at the end. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The header of a `for` loop in Python requires a colon (`:`) at the end.  
# 
# </details>

# #### **Question 1**
# **What happens when you run the code before modifying it? How can you fix this?**

# When running before modifying, it shows a syntax error. to fix, you needed the : at the end of the "for" loop.

# ## Task 2
# In the following code cell, you're provided a list of usernames. There is an issue with the syntax. In this task, you'll run the cell, observe what happens, and modify the code to fix the issue.

# In[5]:


# Assign `usernames_list` to a list of usernames

usernames_list = ["djames", "jpark", "tbailey", "zdutchma" "esmith", "srobinso", "dcoleman", "fbautist"]

# Display `usernames_list`

print(usernames_list)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Each element in `usernames_list` is a username and should be a string. In Python, a string should have quotation marks around it.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# When creating a list in Python, the elements of the list should be separated with commas. There should be a comma between every two consecutive elements. 
# 
# </details>

# #### **Question 2**
# **What happens when you run the code before modifying it? How can you fix it?**

# When trying to run the code, there is a syntax error, and does not let it run. To fix you needed another quotation before esmith.

# ## Task 3
# In the following code cell, there is a syntax error. Your task is to run the cell, identify what is causing the error, and fix it.

# In[6]:


# Display a message in upper case 

print("update needed".upper())


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Calling a function in Python requires both opening and closing parantheses. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# In the code above, check that each function call has both opening and closing parantheses. 
# 
# </details>

# #### **Question 3**
# **What happens when you run the code before modifying it? What is causing the syntax error? How can you fix it?**

# It does not run, you get a syntax error. to fix, you needed a comma at the end to close out the print function.

# ## Task 4
# In the following code cell, you're provided a `usernames_list`, a `username`, and code that determines whether the username is approved. There are two syntax errors and one exception. Your task is to find them and fix the code. A helpful debugging strategy is to focus on one error at a time and run the code after fixing each one.

# In[10]:


# Assign `usernames_list` to a list of usernames that represent approved users

usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username 

username = "esmith"

# For loop that iterates over the elements of `usernames_list` and determines whether each element corresponds to an approved user

for name in usernames_list:

    # Check if `name` matches `username` 
    # If it does match, then display a message accordingly 

    if name == username:
        print("The user is an approved user")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# In Python, the `=` assignment operator allows you to assign or reassign a variable to a value, and the `==` comparison operator allows you to compare one value to another (or the value of one variable to the value of another). 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Indentation is important in Python syntax. Check that the indentation inside the `for` loop and the indentation inside the `if` statement are correct.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Check that each time a variable is used, it's spelled in the same way it was spelled when it was assigned.
# 
# </details>

# #### **Question 4**
# **What happens when you run the code before modifying it? What is causing the errors? How can you fix it?**

# It does not run, as there is a syntax error.
# 
# One error is that they needed to add another = to the if condition. Also, the print at the end needed to be indented. Finally, there needed to be a s at the end of username_list, as username_list is not defined.

# ## Task 5
# 
# In this task, you'll examine the following code and identify the type of error that occurs. Then, you'll adjust the code to fix the error.

# In[13]:


# Assign `usernames_list` to a list of usernames

usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username

username = "eraab"

# Determine whether `username` is the final username in `usernames_list` 
# If it is, then display a message accordingly 

if username == usernames_list[4]:
    print("This username is the final one in the list.")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Recall that indexing in Python starts at `0`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Identify how many elements there are in the `usernames_list`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Since indexing in Python starts at `0` and the `usernames_list` contains `5` elements, identify which index value corresponds to the final element in `usernames_list`.
# 
# </details>

# #### **Question 5**
# **What happens when you run the code before modifying it? What type of error is this? How can you fix it?**

# There is an index error. to fix you need to replace the 5 in the [] to a 4 because there is no 5th on the list, as it is counted starting from 0.

# ## Task 6
# In this task, you'll examine the following code. The code imports a text file into Python, reads its contents, and stores the contents as a list in a variable named `ip_addresses`. It then removes elements from `ip_addresses` if they are in `remove_list`. There are two errors in the code: first a syntax error and then an exception related to a string method. Your goal is to find these errors and fix them.

# In[16]:


# Assign `import_file` to the name of the text file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addressess that are no longer allowed to access the network 

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file and stores its contents as a list in `ip_addresses` 

with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()

# For loop that iterates over the elements in `remove_list`,
# checks if each element is in `ip_addresses`,
# and removes each element that corresponds to an IP address that is no longer allowed

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Display `ip_addresses` after the removal process

print(ip_addresses)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# A `with` statement in Python requires a colon (`:`) at the end of the header.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `.split()` method in Python is used on strings to convert them to lists. To call the `.split()` method, place the string you want to split in front of the method call.
# 
# </details>

# #### **Question 6**
# **What happens when you run the code before modifying it? What is causing the errors? How can you fix them?**

# Invaid syntax error. To fix there needsd to be a : at the end of the with statement. Another thing is that the .split was in the front of ip_addresses instead of after.

# ## Task 7
# In this final task, there are three operating systems: OS 1, OS 2, and OS 3. Each operating system needs a security patch by a specific date. The patch date for OS 1 is `"March 1st"`, the patch date for OS 2 is `"April 1st"`, and the patch date for OS 3 is `"May 1st"`. 
# 
# The following code stores one of these operating systems in a variable named `system`. Then, it uses conditionals to output the patch date for this operating system. 
# 
# However, this code has logic errors. Your goal is to assign the `system` variable to different values, run the code to examine the output, identify the error, and fix it.

# In[19]:


# Assign `system` to a specific operating system as a string

system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system

patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding patch date 

if system == "OS 1":
    print("Patch date:", patch_schedule[0])

elif system == "OS 2":
    print("Patch date:", patch_schedule[1])

elif system == "OS 3":
    print("Patch date:", patch_schedule[2])


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Recall that indexing in Python starts at `0`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Note that the patch dates in `patch_schedule` are in order of operating system. The first patch date in `patch_schedule` corresponds to OS 1, the second patch date in `patch_schedule` corresponds to OS 2, and so on.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Since indexing in Python starts at `0` and `patch_schedule` is in order of operating system from OS 1 to OS 3, the index value `0` corresponds to the patch date for OS 1, the index value `1` corresponds to the patch date for OS 2, and so on.
# 
# </details>

# #### **Question 7**
# **What happens when you run the code before modifying it? What is causing the logic errors? How can you fix them?**

# It runs, the code is fine, but logically it does not make sense. it is supposed to show the date of april 1st, but instead shows a patch date of may 1st. To fix, assign the correct ones on the list, but remember it counts starting from 0.

