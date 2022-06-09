from person import Person

class Student( Person ):
    all_students = []

    def __init__(self, first_name, last_name, age, instructor, current_stack ):
        # Execute the parent class Person constructor and initialize those attributes
        super().__init__(first_name, last_name, age)
        self.instructor = instructor
        self.current_stack = current_stack


    # polymorphism. this will override the print_info of the parent class when called from child class
    def print_info(self):
        super().print_info()
        print("Instructor:", self.instructor)
        print("Current Stack:", self.current_stack)

    @classmethod
    def print_all_students( cls ):
        for Student in cls.all_students:
            Student.print_info()


print("********** MENU ***********")
print("1) Add a new student")
print("2) Show list of all students")
print("0) Exit from program")
option = input(" ")

while option != "0":

    if option == "1":
        first_name = input("Please type your first name:")
        last_name = input("Please type your last name:")
        age = input("Please tpye your age:")
        instructor = input("Please type your instructor's name:")
        current_stack = input("Please type your current stack:")
        new_student = Student(first_name, last_name, age, instructor, current_stack)
        Student.all_students.append(new_student)
    elif option == "2":
        Student.print_all_students()
    else:
        print("Incorrect input. Please try again.")
    





