
"""Module for managing students and their grades."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initialize the student's information."""
        if student_id and name:
            self.student_id = student_id
            self.name = name
            self.gradez = []
            self.is_passed = "NO"
            self.honor = "?"
            self.letter_grade = ""
           
        else:
            print("Missing parameters: 'student_id' and 'name'")

    def add_grades(self, g):
        """Add a grade to the student's grade list."""
        if isinstance(g, (int, float)):
            if g >= 0 and g <= 100:
                self.gradez.append(g)
            else:
                print("Number is out of range")
        else:
            print("Error: Not a number")

    def calc_average(self):
        """Calculate the average of the student's grades."""

        avg = sum(self.gradez) / len(self.gradez)

        if avg < 60:
            self.letter_grade = "F"
        elif avg >= 60 and avg <= 69:
            self.letter_grade = "D"
        elif avg >= 70 and avg <= 79:
            self.letter_grade = "C"
        elif avg >= 80 and avg <= 89:
            self.letter_grade = "B"
        elif avg >= 90 and avg <= 100:
            self.letter_grade = "A"
        return avg

    def check_passed(self):
        if self.calc_average() >= 60:
            self.is_passed = "Passed"
        else:
            self.is_passed = "Failed"

    def check_honor(self):
        """Determine whether the student qualifies for honors."""
        if self.calc_average() >= 60:
            self.honor = True

        else:
            self.honor = False

    def delete_grade_index(self, index):
        """Delete a grade using its index."""
        if index >= 0 and index <= len(self.gradez) - 1:
            del self.gradez[index]
        else:
            print("Error: Index is out of bounds")

    def delete_grade_value(self, value):
        """Delete a grade using its value."""
        if isinstance(value, (int, float)):
            if value in self.gradez:
                del self.gradez[value]
            else:
                print("Value doesn't exists")
        else:
            print("Error: 'value' is not a number")

    def report(self):
        """Display the student's information and academic results."""
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.gradez))
        print("Final Grade:", self.calc_average())
        print("Letter Grade: ", self.letter_grade)
        print("Status: ", self.is_passed)
        print("Honor Roll: ", self.honor)


def startrun():
    """Run the main program."""
    a = Student(1, "Pedro")
    a.add_grades(100)
    a.add_grades("Fifty")  # Broken: invalid grade type
    a.calc_average()
    a.check_honor()
    a.delete_grade_index(5)  # Raises IndexError
    a.report()


startrun()
