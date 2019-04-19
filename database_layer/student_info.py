# this class is to deal with the all info about the student
from row_read import RowRead
class Student:

    def __init__(self, student_id=""):
        """

        :param student_id: 学生的id
        """
        if not len(student_id):
            raise RuntimeError('Pass A StudentId')
        # database
        self.my_data_factory = RowRead()
        self.select_name = {'student_id': 'bf_StudentID'}

        # student id
        self.studentId = student_id

    def get_student_info(self):
        students = self.my_data_factory.read_student_info()
        title = students[0]
        students = students[1:]
        # find the indicator
        id_indicator = title.index(self.select_name['student_id'])
        for student in students:
            if student[id_indicator] == self.studentId:
                return student
        return []


# fangzhou = Student()
# print(fangzhou.get_student_info())
