class Student:
    def __init__(self, student_name, roll_number, class_division, score):
        self.student_name = student_name
        self.roll_number = roll_number
        self.class_division = class_division
        self.score = score

    def display_info(self):
        print(f"Student Name : {self.student_name}")
        print(f"Roll Number  : {self.roll_number}")
        print(f"Division     : {self.class_division}")
        print(f"Marks        : {self.score}")

    def check_result(self):
        status = "Pass" if self.score >= 35 else "Fail"
        print(f"Result       : {status}")
        print("=" * 30)


student1 = Student("Eshwari", 11, "A", 91)
student2 = Student("Pranjal", 12, "A", 67)
student3 = Student("Samruddhi", 13, "A", 29)

student1.display_info()
student1.check_result()

student2.display_info()
student2.check_result()

student3.display_info()
student3.check_result()
