from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Period, Year, Semester, Course, Instructor, Student, Section, Registration


class CourseinfoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester", email="", password="{iSchoolUI}"
        )

        cls.period = Period.objects.create(
            period_id=1,
            period_sequence=1,
            period_name='Spring',
        )

        cls.year = Year.objects.create(
            year_id=1,
            year=2020,
        )

        cls.semester = Semester.objects.create(
            semester_id=1,
            year=Year.objects.get(year=2020),
            period=Period.objects.get(period_name='Spring'),
        )

        cls.course = Course.objects.create(
            course_id=1,
            course_number="IS439",
            course_name="Web Application Using Application Frameworks",
        )

        cls.instructor = Instructor.objects.create(
            instructor_id=1,
            first_name="Kevin",
            last_name="Trainor",
            disambiguator="",
        )

        cls.student = Student.objects.create(
            student_id=1,
            first_name="Meg",
            last_name="Wu",
            disambiguator="",
        )

        # cls.section = Section.objects.create(
        #     section_id=1,
        #     section_name="AOG/AOU",
            # year=Year.objects.get(year=2020),
            # period=Period.objects.get(period_name='Spring'),
        #     instructor=Instructor.objects.get(first_name="Kevin", last_name="Trainor"),
        #
        # )

        # cls.registration = Registration.objects.create(
        #     student_id=1,
        #     first_name="Meg",
        #     last_name="Wu",
        #     disambiguator="",
        # )

    def test_post_model(self):
        self.assertEqual(self.period.period_id, 1)
        self.assertEqual(self.period.period_sequence, 1)
        self.assertEqual(self.period.period_name, "Spring")

    def test_year_model(self):
        self.assertEqual(self.year.year_id, 1)
        self.assertEqual(self.year.year, 2020)

    def test_semester_model(self):
        self.assertEqual(self.semester.semester_id, 1)
        self.assertEqual(self.year.year, 2020)
        self.assertEqual(self.period.period_name, "Spring")

    def test_course_model(self):
        self.assertEqual(self.course.course_id, 1)
        self.assertEqual(self.course.course_number, "IS439")
        self.assertEqual(self.course.course_name, "Web Application Using Application Frameworks")

    def test_instructor_model(self):
        self.assertEqual(self.instructor.instructor_id, 1)
        self.assertEqual(self.instructor.first_name, "Kevin")
        self.assertEqual(self.instructor.last_name, "Trainor")
        self.assertEqual(self.instructor.disambiguator, "")

    def test_student_model(self):
        self.assertEqual(self.student.student_id, 1)
        self.assertEqual(self.student.first_name, "Meg")
        self.assertEqual(self.student.last_name, "Wu")
        self.assertEqual(self.student.disambiguator, "")

    # def test_section_model(self):
    #     self.assertEqual(self.section.section_id, 1)
    #     self.assertEqual(self.section.section_name, "AOG/AOU")
        # self.assertEqual(self.year.year+" - "+self.period.peroid_name, "2021 - Spring")
        # self.assertEqual(self.course.course_number+" - "+self.course.course_name,
        #                  "IS439 - Web Application Using Application Frameworks")
        # self.assertEqual(self.instructor.last_name+" - "+self.instructor.first_name, "Trainor - Kevin")
