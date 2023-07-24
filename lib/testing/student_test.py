# lib/testing/student_test.py
from lib.student import Student
from lib.user import User

class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_student = Student("My", "Student")
        assert (my_student.first_name, my_student.last_name) == ("My", "Student")

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        my_student = Student("My", "Student")
        assert isinstance(my_student.knowledge, list) and len(my_student.knowledge) == 0

    def test_can_learn(self):
        '''learns from a string and adds to self.knowledge.'''
        my_student = Student("My", "Student")
        my_student.learn("New information")
        assert len(my_student.knowledge) == 1
        assert my_student.knowledge[0] == "New information"
