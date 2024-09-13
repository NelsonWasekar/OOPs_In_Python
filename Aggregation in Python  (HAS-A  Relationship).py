#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://www.youtube.com/watch?v=mPFc3JHLnz8      # Aggregation


# In[6]:


class Salary():    # Content
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12) + self.bonus
    
    
class Employee():  # Contanier
    def __init__(self, name, age, salery):
        self.name = name
        self.age = age
        self.obj_salary = salery   # Assign salery class object to data member of Employee class       
        
    def total_salary(self):
        return self.obj_salary.annual_salary()

        
    
salery = Salary(12000, 4000)      # Object of Salary class 

emp = Employee('Nelson', 22, salery)     # Object of Employee class 
print(emp.total_salary())


# In[ ]:




