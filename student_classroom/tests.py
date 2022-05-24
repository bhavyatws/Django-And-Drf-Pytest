from student_classroom.models import Student,Classroom
from mixer.backend.django import mixer  # this create data in database dynamically
import pytest
#not getting data to save in db generated by pytest
pytestmark=pytest.mark.django_db
from hypothesis.extra.django import TestCase
from hypothesis import strategies as st,given

# Create your tests here.

"""Changing AssertEqual to Assert""" 

class StudentModelTestCase(TestCase): # we are not using Default django test case no more
    def test_add_a_plus_b(self):  # function name should always from test
        a = 1
        b = 2
        c = a + b
        # self.assertEqual(c, 3)
        assert c==3

    def test_student_can_be_created(self):
        student1 = Student.objects.create(
            first_name="Shahid", last_name="Gujar", admission_number=123
        )
        student2 = Student.objects.create(
            first_name="Sahid", last_name="Gujar", admission_number=124
        )
        student_last_result = Student.objects.last()
        # self.assertEqual(student_last_result.first_name,"Rahid")
        # self.assertEqual(
        #     str(student_last_result), "Rahids"
        # )  
        # as def __str__ return first_name in string so we can like this also

        #using pytest
        # assert(str(student_last_result)=="Sahid")
        assert student_last_result.first_name=="Sahid"
    
    @given(fail_score=st.floats(min_value=0,max_value=40))
    def test_grade_fail(self,fail_score):
        print("fail score",fail_score)
        student1 = mixer.blend(Student,average_score=fail_score)


        student_last_result = Student.objects.last()
        # self.assertEqual(student_last_result.get_score(), "Fail")
        assert student_last_result.get_score() == "Fail"
    @given(excellent_score=st.floats(min_value=70,max_value=100))
    def test_grade_excellent(self,excellent_score):
        student1 = mixer.blend(Student,average_score=excellent_score)
        student_last_result = Student.objects.last()
        assert student_last_result.get_score() == "Excellent"

    # @given(error_value=st.floats(min_value=101))
    # def test_grade_error(self,error_value):
    #     print(error_value)
    #     student1 = mixer.blend(Student,average_score=error_value)
    #     student_last_result = Student.objects.last()
    #     assert student_last_result.get_score() == "Error"

    # @given(name=st.text())
    # def test_slugify(self,name):
    #     print(name)
    #     student1 = mixer.blend(Student,first_name=name)
    #     student_last_result = Student.objects.last()
    #     assert len(student_last_result.username) == len(name)

class StudentModelUsingSetUpTestCase(TestCase):
    def setUp(self):
        self.student1 = Student.objects.create(
            first_name="Shahid",
            last_name="Gujar",
            admission_number=123,
            average_score=90,
        )

        # setting Up new users
        # getting access tokens / logged in user
        # settng Up timers

    def test_student_can_be_created(self):

        # student_last_result=Student.objects.last()
        # self.assertEqual(student_last_result.first_name,"Rahid")
        # self.assertEqual(
        #     self.student1.first_name, "Shahid"
        # )  # as def __str__ return first_name in string so we can like this also
        assert self.student1.first_name=="Shahid"
    def test_grade_fail(self):

        # self.assertEqual(self.student1.get_score(), "Fail")
        assert self.student1.get_score() == "Fail"

    def test_grade_fail(self):

        # student_last_result=Student.objects.last()
        self.assertEqual(self.student1.get_score(), "Excellent")
        assert self.student1.get_score()=="Excellent"


class StudentModelCreatingDataDTestCase(TestCase):
    def setUp(self):
        # mixer take first argument as model name and second you can specifiy field which you want to test
        #  otherwise randomly all data will generate 
        self.student1 = mixer.blend(Student,average_score=40)

    # def test_student_can_be_created(self):

    #     student_last_result = Student.objects.last()
    #     # self.assertEqual(student_last_result.first_name,"Rahid")
    #     self.assertEqual(
    #         student_last_result.first_name, "Shahid"
    #     )  # as def __str__ return first_name in string so we can like this also

    def test_grade_pass(self):

        student_last_result = Student.objects.last()
        # self.assertEqual(student_last_result.get_score(), "Pass")
        assert student_last_result.get_score() == "Pass"

    # def test_grade_excellent(self):

    #     student_last_result = Student.objects.last()
    #     self.assertEqual(student_last_result.get_score(), "Excellent")

class TestClassroomModel(TestCase):
    # def setUp(self):
    #     self.student1 = Student.objects.create(
    #         first_name="Shahid",
    #         last_name="Gujar",
    #         admission_number=123,
    #         average_score=90,
    #     )
    #     self.classroom1=Classroom.objects.create

    def test_classroom_create(self):
        classroom=mixer.blend(Classroom,name="Physics")
        classroom_result=Classroom.objects.last()
        assert classroom_result.name == "Physics"
