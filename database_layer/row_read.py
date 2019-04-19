import csv
class RowRead:
    """
    数据库读取类
    """
    def __init__(self):
        self.student_info = []

    def read_student_info(self):
        """
        读取指定的 csv
        :return: 一个列表
        """
        # malke a cache
        if not len(self.student_info):
            url = "../dataset/2_student_info.csv"
            csv_file = open(url, "r")
            # read
            reader = csv.reader(csv_file)
            for item in reader:
                item[0] = item[0][-12:]
                self.student_info.append(item)
        return self.student_info
