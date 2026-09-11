class student:
    sub='english'
    college='srist'

stu1=student()
stu2=student()
print(stu1.sub,stu2.sub)

'''using init methode in class and the object'''
class employe:
    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary
emply1=('ashwini',80000)
emply2=('mohit',60000)
print(emply1,emply2)

''' using instance method '''
class student :
    def __init__( self,name,cgpa):
        self.name = name 
        self.cgpa = cgpa

    def get_cgpa(self):
        return self

stu1=student('rahul',8.2)
stu2=student('akash',8.7)

print(stu1.get_cgpa())



'''class attributes and instance attributes '''
class Vidyalay :
    college = 'abc'
    pi=3.1 # class attribute 
    def __init__ (self , name , clas ) :
        self.name =name 
        self.clas = clas 
        self.pi=3.14 # instance attribute 

stu1= Vidyalay('ashwini',12)
print( stu1.pi)
print(Vidyalay.pi)



class Student:
    school_name = "ABC School"  # Class Attribute

    def __init__(self, name):
        self.name = name        # Instance Attribute

    # 1. INSTANCE METHOD
    def show_name(self):
        print("Student Name:", self.name)

    # 2. CLASS METHOD
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

# --- Execution ---
s1 = Student("Ashwini")

s1.show_name()                      # Output: Student Name: Ashwini
Student.change_school("XYZ School") # Modifies class variable globally