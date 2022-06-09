

class Student:
    # Constructor
    def __init__( self, first_name, last_name, instructor, current_stack ):
        # Attributes - accessible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = instructor
        self.current_stack = current_stack

    # methods
    def print_student_info( self ):
        print( "First name:", self.first_name )
        print( "Last name:", self.last_name )
        print( "Instructor:", self.instructor )
        print( "Current Stack:", self.current_stack)


alexander = Student( "Alexander", "Miller", "Alfredo", "Python/Flask" )
alexander.print_student_info()