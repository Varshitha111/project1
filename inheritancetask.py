class course:
    def __init__(self, course_name, price):
        self.course_name = course_name
        self.price = price

    def show_course(self):
        print(f"Course Name: {self.course_name}")
        print(f"Price: {self.price}")

class programmingcourse(course):
    def __init__(self, course_name, price, language):
        super().__init__(course_name, price)
        self.language = language

    def show_programming_course(self):
        self.show_course()
        print(f"Language: {self.language}")
        
ob = programmingcourse("Python", 20000, "English")
ob1 = programmingcourse("Java", 30000, "Telugu")
ob.show_programming_course()
ob1.show_programming_course()