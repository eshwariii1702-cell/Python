# ------------ Decorator ------------

def report_header(func):
    def wrapper(*args, **kwargs):
        print("*" * 50)
        print("LIBRARY REPORT".center(50))
        print("*" * 50)

        func(*args, **kwargs)

        print("*" * 50)
        print("REPORT COMPLETED".center(50))
        print("*" * 50)

    return wrapper


# ------------ Class ------------

class Library:

    library_name = "MIT ADT Central Library"

    def __init__(self, student_name, book_title):
        self.student_name = student_name
        self.book_title = book_title
        self.records = []

    def add_record(self, activity):
        self.records.append(activity)

    @classmethod
    def update_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def welcome():
        print("Library Activity Report")

    def __str__(self):
        return f"Student : {self.student_name}\nBook : {self.book_title}"

    def __len__(self):
        return len(self.records)

    @report_header
    def display_report(self):

        Library.welcome()
        print("Library Name :", Library.library_name)
        print(self)

        print("\nActivity Log:")

        for index, activity in enumerate(self.records, start=1):
            print(f"{index}. {activity}")

        print(f"\nTotal Activities : {len(self)}")


# ------------ Objects ------------

student1 = Library("Eshwari Alapure", "Python Programming")
student1.add_record("Book Issued")
student1.add_record("Completed Unit 1")
student1.add_record("Book Returned")

student2 = Library("Pranjal", "Data Structures")
student2.add_record("Book Issued")
student2.add_record("Renewed for 5 Days")
student2.add_record("Returned Successfully")

student3 = Library("Samruddhi", "Artificial Intelligence")
student3.add_record("Book Issued")
student3.add_record("Completed Reading")
student3.add_record("Book Returned")


# ------------ Menu ------------

while True:

    print("\n========== LIBRARY MENU ==========")
    print("1. Show Report - Student 1")
    print("2. Show Report - Student 2")
    print("3. Show Report - Student 3")
    print("4. Show All Reports")
    print("5. Update Library Name")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student1.display_report()

    elif choice == "2":
        student2.display_report()

    elif choice == "3":
        student3.display_report()

    elif choice == "4":
        student1.display_report()
        student2.display_report()
        student3.display_report()

    elif choice == "5":
        new_name = input("Enter New Library Name: ")
        Library.update_library_name(new_name)
        print("Library name updated successfully!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Please try again.")
