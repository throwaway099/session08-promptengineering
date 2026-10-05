import unittest
from student_utils import calculate_average, is_passing, get_grade


class TestStudentUtils(unittest.TestCase):
    def test_average_of_three_marks(self):
        self.assertEqual(
            calculate_average([80, 90, 100]),
            90.0
        )
    def test_average_of_three_marks_1(self):
        self.assertEqual(
            calculate_average([40]),
            40
        )
    def test_passing_grade(self):
        self.assertEqual(
            is_passing(41),
            True
        )
    def test_passing_grade_1(self):
        self.assertEqual(
            is_passing(40),
            True
        )
    def test_passing_grade_2(self):
        self.assertEqual(
            is_passing(39),
            False
        )
    def test_grades(self):
        self.assertEqual(
            get_grade(95),
            "Distinction"
        )
    def test_grades_1(self):
        self.assertEqual(
            get_grade(60),
            "First"
        )
    def test_grades_2(self):
        self.assertEqual(
            get_grade(45),
            "Second"
        )
    def test_grades_3(self):
        self.assertEqual(
            get_grade(30),
            "Fail"
        )

    

    # Add one test method per specification row.
    # Name each method after what it checks.


unittest.main(argv=[""], exit=False)
