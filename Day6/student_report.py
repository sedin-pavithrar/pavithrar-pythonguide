# Student Report Card -- Encapsulation
# encapsulation __private @property validation
# Real-world App
# CBSE / Extramarks
# Overview
# All data is private via name-mangling (__name, __marks). @property creates read-only getters for 
# name, percentage, and grade. add_marks() validates range 0-100 and rejects duplicates. 
# Demonstrates why direct attribute access is dangerous and how @property provides a clean public 
# API -- the same pattern used in Django model fields.
# Problem
# Student class with private marks. @property for read-only access. Reject invalid marks (< 0 or > 
# 100).
# Starter Code
# class Student:
#     def __init__(self, name, roll_no):
#         self.__name=name; self.__roll_no=roll_no
#         self.__marks={}  # private
#     @property
#     def name(self): return self.__name
#     def add_marks(self, subject, marks): ...
#     @property
#     def percentage(self) -> float: ...
#     @property
#     def grade(self) -> str: ...
# Constraints
# •  All __ attrs private -- no direct outside access
# •  add_marks rejects < 0 or > 100 and duplicates
# •  percentage and grade are read-only @property
# Bonus:  Add __gt__ to compare two students by percentage


class Student:
    def __init__(self, name, roll_no):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks={}  
    @property
    def name(self): 
        return self.__name
    @property
    def roll_no(self):
        return self.__roll_no
    
    def add_marks(self, subject, marks): 
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        if subject in self.__marks:
            raise ValueError("Marks for this subject already added ")
        
        self.__marks[subject] = marks

    @property
    def percentage(self) -> float: 
        if not self.__marks:
            return 0.0
        total = sum(self.__marks.values())
        return total /len(self.__marks)
    @property
    def grade(self) -> str: 
        p = self.percentage

        if p >= 90:
            return "A+"
        elif p>= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        return "F"

    def __gt__(self, other):
        return self.percentage > other.percentage

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"Percentage: {self.percentage:.2f}%\n"
            f"Grade: {self.grade}"
        )
def main():
    s1 = Student("Arun", 101)
    s1.add_marks("Math", 95)
    s1.add_marks("Science", 88)
    s1.add_marks("English", 92)
    print(s1)

if __name__ == "__main__":
    main()
