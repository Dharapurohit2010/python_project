#########1########
class Student:
    schoolName= "Global School"
    schoolAddress="Chennai"
    def __init__(self,studentRollno=None,studentName=None,studentPercentage=None ):
        self.studentRollno = studentRollno
        self.studentName = studentName
        self.studentMailid = None
        self.studentPercentage = studentPercentage
        self.schoolName = None
        self.schoolAddress= None

    def print_grade(self):
        if self.studentPercentage > 100 or self.studentPercentage < 0:
            print("Invalid input")
        elif self.studentPercentage >= 90:
            print( "Grade A")
        elif self.studentPercentage >= 80 and self.studentPercentage <= 89:
            print( "Grade B")
        elif self.studentPercentage >= 60 and self.studentPercentage <= 79:
            print("Grade C")
        else:
            print("Failed, Please re-attempt")
    def get_student_name(self):
        return self.schoolName
    @property
    def get_name_with_percentage(self):
        return "Hi, "+str(self.studentName)+"-your percentage is  " + str(self.studentPercentage)

