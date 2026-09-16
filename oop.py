# class student:
#     sub='english'
#     college='srist'

# stu1=student()
# stu2=student()
# print(stu1.sub,stu2.sub)

# '''using init methode in class and the object'''
# class employe:
#     def __init__(self,name,salary,):
#         self.name=name
#         self.salary=salary
# emply1=('ashwini',80000)
# emply2=('mohit',60000)
# print(emply1,emply2)

# ''' using instance method '''
# class student :
#     def __init__( self,name,cgpa):
#         self.name = name 
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self

# stu1=student('rahul',8.2)
# stu2=student('akash',8.7)

# print(stu1.get_cgpa())



# '''class attributes and instance attributes '''
# class Vidyalay :
#     college = 'abc'
#     pi=3.1 # class attribute 
#     def __init__ (self , name , clas ) :
#         self.name =name 
#         self.clas = clas 
#         self.pi=3.14 # instance attribute 

# stu1= Vidyalay('ashwini',12)
# print( stu1.pi)
# print(Vidyalay.pi)



# class Student:
#     school_name = "ABC School"  # Class Attribute

#     def __init__(self, name):
#         self.name = name        # Instance Attribute

#     # 1. INSTANCE METHOD
#     def show_name(self):
#         print("Student Name:", self.name)

#     # 2. CLASS METHOD
#     @classmethod
#     def change_school(cls, new_school):
#         cls.school_name = new_school

# # --- Execution ---
# s1 = Student("Ashwini")

# s1.show_name()                      # Output: Student Name: Ashwini
# Student.change_school("XYZ School") # Modifies class variable globally


# '''above decoreter @classmethod is used to peform thhe proper work of the (cls )'''



# ''''init method is canot be used more then one time in a class '''
# class student:
#     college_name='asd'
#     def __init__ (self,name,clas):# if we use ix in place of init then we have to call it manually
#         self.name=name
#         self.clas=clas
#     def ix (self):
#         print('e')

        
# st=student('ashwi',12)

# print(st.name)


# 'classmethod practice'
# class student:
#     college_name='asd'
#     def __init__ (self,name,clas):
#         self.name=name
#         self.clas=clas
#     def ix (self):
#         print('e')
#     @classmethod
#     def colg(cls,college_name):
#         cls.college_name=college_name
#         print(cls.college_name)

        
# stu2=student('solo',12)

# stu2.colg('kvs')
# print(stu2.college_name)

# '''using staticmethod'''
# class Student:
#     school = "ABC School"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

#     @staticmethod
#     def is_adult(age):
#         return age >= 18


# student1 = Student("Rahul", 20)

# Student.change_school("XYZ School")
# print(Student.school)                 # XYZ School
# print(Student.is_adult(student1.age)) # True


''' creating a online store for the products(name,price)'''

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def data(self):
        return(f" name of product {self.name},price{self.price}")

    
p2=product('ram',45)
print(p2.data())