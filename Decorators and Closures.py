# -------------------- Decorator 1 --------------------
def access_granted(func):
    def wrapper(*args, **kwargs):
        print("Access Granted")
        return func(*args, **kwargs)
    return wrapper


# -------------------- Decorator 2 --------------------
def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"Activity Recorded: Profile opened for {args[0].student_name}")
        return func(*args, **kwargs)
    return wrapper


# -------------------- Student Class --------------------
class Student:
    def __init__(self, student_name, roll_number, student_code, department):
        self.student_name = student_name
        self.roll_number = roll_number
        self.student_code = student_code
        self.department = department

    @access_granted
    @log_activity
    def display_profile(self):
        print("\n------ Student Details ------")
        print("Name       :", self.student_name)
        print("Roll No    :", self.roll_number)
        print("Student ID :", self.student_code)
        print("Department :", self.department)
        print("-----------------------------")


# -------------------- Closure --------------------
def create_message(message):
    def display(student):
        print(message + student.student_name)
    return display


# -------------------- Creating Objects --------------------
student1 = Student("Eshwari", 1, "SOC101", "Computer Science")
student2 = Student("Pranjal", 2, "SOC102", "Computer Science")
student3 = Student("Samruddhi", 3, "SOC103", "Computer Science")


# -------------------- Display Profiles --------------------
student1.display_profile()
print()

student2.display_profile()
print()

student3.display_profile()
print()


# -------------------- Closure Functions --------------------
welcome = create_message("Welcome, ")
hello = create_message("Hello, ")
best_wishes = create_message("Best Wishes, ")


# -------------------- Using Closures --------------------
welcome(student1)
hello(student2)
best_wishes(student3)
