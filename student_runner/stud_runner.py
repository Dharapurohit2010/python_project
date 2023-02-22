from student_package.student_type import Student

stu_1= Student()
stu_2= Student()
stu_3= Student()
####Student1#####
stu_1.studentRollNo=1001
stu_1.studentName="jack"
stu_1.studentMailid="jack@gmail.com"
stu_1.studentPercentage=45.2
#######Student2####
stu_2.studentRollNo=1002
stu_2.studentName="peter"
stu_2.studentMailid="peter@gmail.com"
stu_2.studentPercentage=85.2
#######Student3####
stu_3.studentRollNo=1003
stu_3.studentName="mark"
stu_3.studentMailid="mark@gmail.com"
stu_3.studentPercentage=56.5

print(stu_1.studentMailid)
print(stu_2.studentMailid)
print(stu_3.studentMailid)
#stu_1= stu_2
print(stu_1)
print(stu_2)
print(stu_3)

####loading data####
stu_1=Student(101,"sjj",45)
stu_2=Student(102,"Peter")
stu_3=Student(103,"Mark")
name= stu_1.studentName
print(name)

output = stu_1.get_name_with_percentage()
print(output)







