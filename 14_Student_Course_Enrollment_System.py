# 14 - Student Course Enrollment System

# You are tasked with designing a system to manage student course enrollments. Create Python classes for Student,
# Course, and EnrollmentManager. The goal is to allow students to enroll in courses, drop courses, and view their
# course schedules.
#
# Student Class:
#
# Attributes:
# Student ID (integer)
# First Name (string)
# Last Name (string)
# Methods:
# __init__(self, student_id: int, first_name: str, last_name: str): Initialize a student with an ID, first name, and last name. The student should have an empty schedule initially.
# Course Class:
#
# Attributes:
# Course Code (string)
# Course Name (string)
# Maximum Capacity (integer)
# Current Enrollment (integer, initially set to 0)
# Student List (a list to store student IDs)
# Methods:
# __init__(self, course_code: str, course_name: str, max_capacity: int): Initialize a course with a course code, course name, and maximum capacity. The course should have an empty student list initially.
# enroll_student(self, student_id: int) -> str: Attempt to enroll a student in the course. If successful, return "Enrollment successful." If the course is full, return "Course is full; enrollment failed."
# drop_student(self, student_id: int) -> str: Attempt to drop a student from the course. If successful, return "Student dropped." If the student is not enrolled in the course, return "Student not found in the course."
# get_course_info(self) -> str: Return course information, including code, name, current enrollment, and maximum capacity.
# EnrollmentManager Class:
#
# Attributes:
# Students (a list to store Student objects)
# Courses (a list to store Course objects)
# Methods:
# add_student(self, student: Student): Add a student to the list of students.
# add_course(self, course: Course): Add a course to the list of courses.
# enroll_student(self, student_id: int, course_code: str) -> str: Enroll a student in a course by their ID and course code. Return appropriate messages as mentioned in the Course class methods.
# drop_student(self, student_id: int, course_code: str) -> str: Drop a student from a course by their ID and course code. Return appropriate messages as mentioned in the Course class methods.
# view_student_schedule(self, student_id: int) -> List[str]: Given a student's ID, return a list of course codes for the courses in which the student is enrolled.
# view_course_enrollment(self, course_code: str) -> List[int]: Given a course code, return a list of student IDs for the students enrolled in the course.


class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.schedule = []

    def add_course(self, course_code: str):
        self.schedule.append(course_code)
        return f'Course {course_code} added to the schedule.'

    def drop_course(self, course_code: str):
        if course_code in self.schedule:
            self.schedule.remove(course_code)
            return f'Course {course_code} dropped from the schedule.'
        else:
            return f'Course {course_code} not found in the schedule.'

    def get_courses(self):
        return self.schedule

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Course:
    def __init__(self, course_code, course_name, max_capacity):
        self.course_code = course_code
        self.course_name = course_name
        self.max_capacity = max_capacity
        self.current_enrollment = 0
        self.student_list = []

    def enroll_student(self, student_id: int):
        if self.current_enrollment < self.max_capacity:
            self.student_list.append(student_id)
            self.current_enrollment += 1
            return "Enrollment successful."
        else:
            return "Course is full; enrollment failed."

    def drop_student(self, student_id: int):
        if student_id in self.student_list:
            self.student_list.remove(student_id)
            self.current_enrollment -= 1
            return "Student dropped."
        else:
            return "Student not found in the course."

    def get_course_info(self):
        return f'Course: {self.course_code} - {self.course_name} (Enrolled: {self.current_enrollment}/{self.max_capacity})'


class EnrollmentManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student: Student):
        """Add a student to the list of students."""
        self.students.append(student)
        print('Student Successfully Added.')

    def add_course(self, course: Course):
        """ Add a course to the list of courses."""
        self.courses.append(course)
        print('Course Successfully Added.')

    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course by their ID and course code. Return appropriate messages as mentioned in the
        Course class methods."""
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s
                break

        course = None
        for c in self.courses:
            if c.course_code == course_code:
                course = c
                break

        if student is not None and course is not None:
            result = course.enroll_student(student_id)
            return result
        else:
            return 'Student and Course not found.!'

    def drop_student(self, student_id, course_code):
        """Drop a student from a course by their ID and course code. Return appropriate messages as mentioned in the
        Course class methods."""
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s
                break

        course = None
        for c in self.courses:
            if c.course_code == course_code:
                course = c
                break

        if student is not None and course is not None:
            result = course.drop_student(student_id)
            return result
        else:
            return 'Student and Course Not Found.!'

    def view_student_schedule(self, student_id):
        """ Given a student's ID, return a list of course codes for the courses in which the student is enrolled."""
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s
                break

        if student is not None:
            result = student.get_courses()
            return result
        else:
            return "Student not found.!"

    def view_course_enrollment(self, course_code: str):
        """Given a course code, return a list of student IDs for the students enrolled in the course."""
        course = None
        for c in self.courses:
            if c.course_code == course_code:
                course = c
                break

        if course is not None:
            result = course.student_list
            return result
        else:
            return "Course not found.!"


# Create students
student1 = Student(1, "Alice", "Johnson")
student2 = Student(2, "Bob", "Smith")

# Create courses
course1 = Course("CSCI101", "Introduction to Computer Science", 30)
course2 = Course("MATH202", "Calculus II", 25)

# Create an enrollment manager
manager = EnrollmentManager()

# Add students and courses to the manager
manager.add_student(student1)
manager.add_student(student2)
manager.add_course(course1)
manager.add_course(course2)

# Enroll students in courses
print(manager.enroll_student(11, "CSCI101"))  # Enrollment successful.
print(manager.enroll_student(2, "MATH202"))  # Enrollment successful.
print(manager.enroll_student(10, "MATH202"))  # Course is full; enrollment failed.

# View student schedule and course enrollment
print(manager.view_student_schedule(11))  # ['CSCI101']
print(manager.view_course_enrollment("MATH202"))  # [2]
