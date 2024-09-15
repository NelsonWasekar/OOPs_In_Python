#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://www.youtube.com/watch?v=lhiH-6ygGl8&t=290s    


# In[5]:


class Salary():    # Content
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12) + self.bonus
    
    
class Employee():  # Contanier
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)  # Call of Salary class
        
    def total_salary(self):
        return self.obj_salary.annual_salary()

            
emp = Employee('Nelson', 22, 12000, 4000)   
print(emp.total_salary())


# In[7]:


12000*12+4000


# In[ ]:




