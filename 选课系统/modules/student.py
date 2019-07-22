class Student(object):
    '''
    学生类
    '''
    def __init__(self, stu_name, stu_age):
        self.name = stu_name
        self.age = stu_age
        self.grade = {}
        self.student_class = {}



    def student_add_class(self, class_name, class_obj):

        self.student_class[class_name] = class_obj



    def student_add_grade(self, grade, student_obj):
        self.garde[grade] = student_obj

