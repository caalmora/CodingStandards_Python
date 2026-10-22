
"""Module for managing students and their grades."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initialize the student's information."""
        self.student_id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        """Add a grade to the student's grade list."""
        self.gradez.append(g)

    def calc_average(self):
        """Calculate the average of the student's grades."""
        return sum(self.gradez) / len(self.gradez)

    def check_honor(self):
        """Determine whether the student qualifies for honors."""
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Delete a grade using its index."""
        del self.gradez[index]

    def report(self):
        """Display the student's information and academic results."""
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.gradez))
        print("Final Grade:", self.calc_average())

def startrun():
    """Run the main program."""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # Broken: invalid grade type
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # Raises IndexError
    a.report()

startrun()
