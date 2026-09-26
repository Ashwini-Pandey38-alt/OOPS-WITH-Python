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


# ''' creating a online store for the products(name,price)'''

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def data(self):
#         return(f" name of product {self.name},price{self.price}")

    
# p2=product('ram',45)
# print(p2.data())



# '''tracking the total product being created'''


# class product:
#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1
#     def data(self):
#         return(f" name of product {self.name},price{self.price}")
#     @classmethod
#     def info(cls):
#         return f" no. of product is made{cls.count}"

    

# p3=product('loko',45)
# p4=product('water bottel',100)
# product.info()



# '''code to claculate the max discount in the product'''
# class product:

#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1
#     def data(self):
#         return(f" name of product {self.name},price{self.price}")
#     @classmethod
#     def info(cls):
#         return f" no. of product is made{cls.count}"
#     @staticmethod
#     def get_dic( price,percentage):
#         return f" discount={price-(price*percentage)}"

    
# product.get_dic(2000,2)
# ' discount=-2000'


# '''4  PILLERS OF THE OOP'S 
# 1.Encapsulation
# 2.Inheritence 
# 3.Abstraction
# 4.Polymorphism'''



# # ENCAPSULATION
# class banks:
#     def __init__(self,name,balance):
#         self.name=name 
#         self.balance=balance #public

# class banks:
#     def __init__(self,name,balance):
#         self.name=name 
#         self._balance=balance #protected

# class banks:
#     def __init__(self,name,balance):
#         self.name=name 
#         self.__balance=balance #private



# #DIFFERENT WAY TO ACCESS THE PROTECTED AND THE PRIVATE DATA
# # FOR THE PROTECTED DATA
# print("object_name._DataName")

# # FOR THE PRIVATE DATA

# print("object_name.classname__DataName")

# #REAL way to access the private data
# """GETTER AND SETTER METHOD"""
# class banks:
#     def __init__(self,name,balance):
#         self.name=name 
#         self.__balance=balance #private
#     def gett(self):
# #         return self.__balance
# #     def setter(self,new):
# #         self.__balance=new




# #INHERITANCE
# #single level inheritence
# class school:
#     def __init__(self,name,location):
#         self.name=name
#         self.location=location


        
# class teacher(school):
#     def __init__(self,nam,salary,name,location):
#         super().__init__(name,location)
#         self.nam=nam
#         self.salary=salary

        
# teacher('rahul',20000,'kf','sk')

# p=teacher('rahul',20000,'kf','sk')
# print(p.name)
# #kf
        

# # multi level inheritence
# class teacher(school):
#     def __init__(self,nam,salary,name,location):
#         super().__init__(name,location)
#         self.nam=nam
#         self.salary=salary

        

        
# class student(teacher):
#     def __init__(self,na,nam,salary,name,location):
#         super().__init__(nam,salary,name,location)
#         self.na=na

        
# o=student('s','ss','sss','ssss','sssss')
# print(o.salary)

# # MULTIPLE INHERITENCE

# class teacher:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

        
# class stu:
#     def __init__(self ,cgpa):
#         self.cgpa=cgpa



        


# class school(teacher,stu):
#     def __init__(self,name,salary,cgpa):
#         super().__init__(name,salary)
#         stu.__init__(self,cgpa)# second time did not have to use the super() function

        
# y=school("dd",200000,9.3)
# print(y.cgpa)
# #9.3



# #abstraction
# from abc import ABC ,abstractmethod
# class animal (ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass



# class loin (animal):
#     def make_sound(self):
#         print('rooooooooorrrrrrrr')

        
# t=loin()
# print(t)
# t.make_sound()
# #rooooooooorrrrrrrr
# class cow(animal):
#     def make_sound(self):
#         print('mooooooooooooooooooooooooooooooooo')

        
# u=cow()
# u.make_sound()
# #moooooooooooooooooooooooooooooooo





# Polymorphism
# 1.function overloading



# class teacher:                                   
#     def postion(self):
#         print('work as teacher')

# class stu:
#     def postion(self):
#         print('study as an the student')

# #2.duck typing

# class teacher:                                   
#     def postion(self):
#         print('work as teacher')

# class stu:
#     def postion(self):
#         print('study as an the student')




# '''. Create a bankaccount class with account no.,owner name,balance
# add also use methods like DEPOSIT,WITHDROW,CHECK BALANCE'''


# class bankaccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.balance=balance
#     def deposit(self,nbalance):
#         self.balance=self.balance+nbalance
#     def withdrow(self,wanted):
#         self.balance=self.balance-wanted
#     def check_balance(self):
#         print('present_balance=',self.balance)

        
# t=bankaccount(20000332,'ashwini',200_0000)
# t.check_balance()
# #present_balance= 2000000

# '''Create a class BOOK with the following attributes:
# title 
# author 
# list of reviews
# And add methods to: 
# add a new review 
# count reviews 
# display all reviews'''
# class book:
#     count=0
#     def __init__(self,title,auther, reviews,number_of_reviews):
#         self.title=title
#         self.auther=auther
#         self.reviews=reviews
#         self.count=number_of_reviews

#     def add(self,N,number_of_reviews):
#         self.reviews= self.reviews+N
#         self.count=self.count+number_of_reviews

#     def cont(self):
#         print(  self.count )
#     def dis(self):
#         print(self.reviews)

        
# t=book('s','ss','sss',1)
# t.add('----hello',1)
# t.cont()
# #2
# t.dis()
# #sss----hello

# '''Create a class  with  attributes _name, _roll_no, and _marks.
# Provide  and  methods with validation (e.g., marks cannot be 
# negative, roll number has to be between 1 & 100 & name cannot be empty)'''
# class kaksha :

#     def  __init__(self , name ,rollno ,marks):
#         self.name=name
#         self.rollno=rollno
#         self.__marks=marks
#     def get(self):     # getter and the setter method for the marks
#         print(self.__marks)
#     def setter (self):
#         if self.__marks>=0:
#             print(self.__marks)
#         else:
#             print ('marks cannot be the negative number ')
#     def getter(self):     # getter and the setter method for the roll number
#         print(self.rollno)
#     def sette(self):
#         if self.rollno>=1 and self.rollno<=100:
#             print(self.rollno)
#         else:
#             print ('rollnumer is not between 1 and 100')
#     def gett(self):     # getter and the setter method for the name
#         print(self.name)
#     def sett(self):
#         if self.name=="":

#             print('name cannot be an empty')
#         else:
#             print (self.name)



# '''Create a class shape with a method area().'''
# # Create subclasses circle , rectangle , and triangle  that  overraid the area() 
# # method.
# # 
# class shape:
#     def __init__(self ,length,breadth):

#         self.length=length
#         self.breadth=breadth

        
# class circle(shape):
#     def __init__(self ,radius):
#         self.radius=radius
#     def area (self):
#         print(3.14*(self.radius**2))


# class rectangle(shape):
#     def __init__(self,length,breadth):
#         super().__init__(length,breadth)
#     def area(self):
#         print(self.length*self.breadth)


# class triangle(shape):
#     def __init__(self,length,breadth):
#         super().__init__(length,breadth)
#     def area(self):
#         print(0.5*(self.length*self.breadth))


# o=circle(5)
# o.area()

# o=rectangle(20,30)
# o.area()

# o=triangle(20,30)
# o.area()




# #WAP to search the word in file

# with open ('sample.txt','r') as f:
#     line=1
#     while True :
#         data = f.readline()
#         if ('python'in data):
#             print('word is found at the line',line)
#         line+=1


# '''5 base
# Vehicle
# subclasses
# Car Bike
# . Create a  class  with attributes like brand and model.
# Create two  and  that add extra attributes - seats (in Car) & 
# engine_cc (in Bike)'''

# class vehicle:
#     def __init__(self,brand,modle):
#         self.brand=brand
#         self.modle=modle

# class car(vehicle):
    
#     def __init__(self,brand,modle ,seats):
#         super().__init__(brand,modle)
#         self.seats=seats

# class bike(vehicle):
    
#     def __init__(self,brand,modle ,engine):
#         super().__init__(brand,modle)
#         self.engine=engine

# x = vehicle("Toyota","Alcazar")
# y= car("Toyota","Alcazar","4 Seater")
# print(y.brand)
# print(x.modle)
# print(y.seats)
# print(x.modle)

'''WAO TO CALCULATE THE SALARY OF DIFFERENT EMPLOYEE'''
class employee:
    def __init__(self,inhand_salary,gst):
        self.inhand_salary=inhand_salary
        self.gst=gst
    def cal_salary(self):
        print("THE CALCULATED AMOUNT OF THE SALARY IS =====",self.inhand_salary-self.gst)

class intern(employee):
    def __init__(self,inhand_salary,gst):
        super().__init__(inhand_salary,gst)

    def cal_salary(self):
            print("THE CALCULATED AMOUNT OF THE SALARY IS =====",self.inhand_salary-self.gst)




class fulltimeemployee(employee):
    def __init__(self,inhand_salary,gst,bonus,overtime,traveling_amount):
        
        super().__init__(inhand_salary,gst)
        self.bonus=bonus
        self.overtime=overtime
        self.traveling_amount=traveling_amount

    def cal_salary(self):
            print("THE CALCULATED AMOUNT OF THE SALARY IS =====",self.inhand_salary-self.gst+self.bonus+self.overtime+self.traveling_amount)



class contractbased(employee):
    def __init__(self,inhand_salary,gst,bonus):

        super().__init__(inhand_salary,gst)
        self.bonus=bonus

    def cal_salary(self):
            print("THE CALCULATED AMOUNT OF THE SALARY IS =====",self.inhand_salary-self.gst+self.bonus)
    
x=employee(20000,20)
x.cal_salary()
y=fulltimeemployee(20000,20,5000,6000,8000)
y.cal_salary()
