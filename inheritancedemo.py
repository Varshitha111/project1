# class Course:
#     course_name=""
#     price=0
#     def __init__(self,course_name,price):
#         self.course_name=course_name
#         self.price=price
#     def show_course(self):
#         print(self.course_name,self.price)
# class ProgrammingCourse(Course):
#     language=""
#     duration=""
#     def __init__(self,course_name,price,language,duration):
#         super().__init__(course_name,price)
#         self.duration=duration
#         self.language=language
#     def show_programming_course(self):
#         super().show_course()
#         print(self.language,self.duration)
# ob=ProgrammingCourse("python",20000,"english","1 month")
# ob.show_programming_course()
# ob1=ProgrammingCourse("java",30000,"telugu","2 months")
# ob1.show_programming_course()

# syntax 
# class cl_name :
#     # attr
#     # __init__ 
#     # meth1 function
#     #methd2 function
# o=cl_name()
# o.attr
# o.meth1()
# o.mehd2()


# inheritance  p - c

class A:
    clName="A" # class variable

    def __init__(self): # def method
        self.name="srinu"
        # instance varaible
        print("a class init method")

    def height_A(self): # instance #instance varaibles
        self.height=5.6 # instance variables
        print(self.height)

    def land_A(self):
        self.land="2acre"
        print(self.land)    

class B(A):
    clName="B"

    def __init__(self):
        print("b class init method") 

    def acquireChars(self):
        super().__init__()
        print("acquireChars method")  
        print(super().clName) # acquiring r accessing r using parent class attr
        super().height_A()  #acquiring r accessing r using parent class defined method :-- using :-- 
        super().height_A() # :-- reusability
        super().land_A()

o=B()  #obj creation  
print(o.clName) # accessing b class attribute with the help of o object and which is b class instance 
o.acquireChars()