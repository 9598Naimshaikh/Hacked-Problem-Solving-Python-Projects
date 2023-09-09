# 11-: Student and Course Management

# Create two Python classes, Student and Course, to manage students and their courses. Here are the specifications for each class:
# Student Class:

# Attributes:
# Student ID
# First Name
# Last Name
# Courses (a list of course codes)

# Methods:
# __init__(self, student_id: int, first_name: str, last_name: str): Initialize a student with an ID, first name, and last name. The list of courses should be empty initially.
# add_course(self, course_code: str): Add a course to the student's list of courses.
# remove_course(self, course_code: str): Remove a course from the student's list of courses.
# get_courses(self) -> List[str]: Return a list of course codes that the student is enrolled in.
# get_full_name(self) -> str: Return the full name of the student (e.g., "John Doe").
# Course Class:

# Attributes:
#
# Course Code
# Course Name
# Students (a list of student IDs)

# Methods:
# __init__(self, course_code: str, course_name: str): Initialize a course with a code and name. The list of students should be empty initially.
# add_student(self, student_id: int): Add a student to the course's list of students.
# remove_student(self, student_id: int): Remove a student from the course's list of students.
# get_students(self) -> List[int]: Return a list of student IDs enrolled in the course.
# get_course_info(self) -> str: Return course information including code and name (e.g., "Course: COMP101 - Introduction to Programming").


class Student:
    def __init__(self, student_id, f_name, l_name):
        """Initialize a student with an ID, first name, and last name. The list of courses should be empty initially"""
        self.student_id = student_id
        self.f_name = f_name
        self.l_name = l_name
        self.courses = []

    def add_course(self, course_code):
        """Add a course to the student's list of courses"""
        self.courses.append(course_code)
        print(f'{course_code!r} Course have been successfully added.!')

    def remove_course(self, course_code):
        """Remove a course from the student's list of courses."""
        for course in self.courses:
            if course_code == course:
                print(course_code)
                return
        print(f'{course_code} NOT Found.!')

    def get_courses(self):
        """Return a list of course codes that the student is enrolled in."""
        return f'Courses: {self.courses}'

    def get_full_name(self):
        """str: Return the full name of the student (e.g., "John Doe")"""
        name = str(self.f_name), str(self.l_name)
        name = ' '.join(name)
        return f'Student Name: {name}'


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []

    def add_student(self, student_id):
        """Add a student to the course's list of students."""
        self.students.append(student_id)
        print(f'Student: {student_id} added successfully.!')

    def remove_student(self, student_id):
        """Remove a student from the course's list of students."""
        for std_id in self.students:
            if std_id == student_id:
                self.students.remove(student_id)
                return
        print(f'Sorry.! Student: {student_id} NOT Found.!')

    def get_student(self):
        """Return a list of student IDs enrolled in the course."""
        return self.students

    def get_course_info(self):
        """Return course information including code and name (e.g., "Course: COMP101 - Introduction to Programming")."""
        return f'Course: {self.course_code} - {self.course_name}'


std1 = Student(112, 'Naim', 'Shaikh')
std2 = Student(222, 'Samad', 'Shaikh')

course1 = Course("BCA", 'Computer Science')
course2 = Course("B-Tech", "Software engineering")

std1.add_course('BCA')
std1.add_course('B-Tech')

std1.remove_course('BA')
# print(std1.remove_course.__doc__)

std1.get_courses()
print(std1.get_full_name())

course1.add_student(11232)
course2.add_student(2334)

course1.remove_student(132)

print(course1.get_student())
print(course2.get_student())

print(course1.get_course_info())
print(course2.get_course_info())