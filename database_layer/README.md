## 怎么用底层类获得信息

1. 用之前先引入类Student

    ~~~python
    from student_info import Student
    ~~~



2. 初始化类既可以利用学号获得相应信息

   ~~~python
   # 构造的时候传入学号
   FangZhou = Student("14635")
   
   # 如果没有传入学号 会抛出异常
   #FangZhou = Student()
   #RuntimeError: No StudentId
   
   # 成功初始化之后调用函数get_student_info, 则可以以列表的形式获得这个学生的信息, 如果没找的则返回[]
   FangZhou.get_student_info()
   ~~~


