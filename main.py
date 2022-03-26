'''
Written by: Sam Platt for 2022 Hackathon
Date: Mar 26, 2022
Email: platts1@sou.edu
'''

class Course:
  def __init__(self, name, credits, grade, points):
    self.name = name
    self.credits = credits
    self.grade = grade
    self.points = points

def get_points(credits, grade):
    grade_points = {
        "A": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1,
        "D-": 0.7,
        "F": 0
    }
    return (credits * grade_points[grade])

def enter_courses(num_courses):
    course_list = list()
    course_names = list()

    for i in range(num_courses):

        course_name = input("\nEnter the name of a course: ")
        while course_name in course_names:
            course_name = input("You've already entered this course. Enter the name of a different course: ")

        course_credits = int(input("Enter how many credits {name} is worth: ".format(name = course_name)))
        course_grade = input("Enter your letter grade in {name}: ".format(name = course_name))
        course_points = get_points(course_credits, course_grade)
        
        course_names.append(course_name)
        course_list.append(Course(course_name, course_credits, course_grade, course_points))

    print("Course information entered:\n")
    for course in course_list:
        print("Name: {name}\tGrade: {grade}\tCredits: {credits}\n".format(name = course.name, grade = course.grade, credits = course.credits))
    
    return course_list


def main():
    print("Welcome to the GPA calculator.\nPlease follow the instructions below to calculate your GPA.\nNote: Do not enter course information for P/NP courses\n")

    num = int(input("Enter the number of classes: "))
    
    course_list = enter_courses(num)
    
    total_points_earned = 0
    total_points_possible = 0
    for course in course_list:
        total_points_earned += course.points
        total_points_possible += course.credits

    gpa = total_points_earned / total_points_possible
    print("Your GPA is {gpa:.2f}".format(gpa = gpa))

if __name__ == "__main__":
    main()