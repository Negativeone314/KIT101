"""
6.2CR Dictionaries (Student GPA Calculator)
"""

__author__ = "Thomas Couser"


def check_id(dict: dict, id: str):
    """Checks if a student ID exists in the dictionary"""
    id: str # student ID
    
    if id in dict:
        return True
    else:
        return False


def add_student(dict: dict, id: str):
    """Adds a new student to the dictionary"""
    id: str # student ID
    results: int # student results
    
    if check_id(dict, id):
        print("Student already exists")
    else:
        result = int(input("Enter result: "))
        results = []
        results.append(result)
        dict[id] = results


def display_students(dict: dict):
    """Displays all students and their results"""
    if len(list(dict)) == 0:
        print("There are no students in the dictionary")
    else:
        print(f"Displaying students and results for {len(list(dict))} record(s): ")
        
        for student, results in dict.items():
            print(f"Student '{student}'", end=" ")
            print(f"results: {results}")
        print("")


def add_result_for_student(dict: dict, id: str):
    """Adds a new result for a student that already exists"""
    id: str # student ID
    result: int # student result
    
    if check_id(dict, id):
        result = int(input("Enter result: "))
        dict[id].append(result)
        print("Result added")
    else:
        print("Student does not exist")


def calculate_average(dict: dict, id: str):
    """Calculates the average of a student's results"""
    id: str # student ID
    total: int # total of student results
    average: float # average of student results
    
    if check_id(dict, id):
        total = sum(dict[id])
        average = total / len(dict[id])
        print(f'Average of student {id}: {average}')
        return average
    else:
        print("Student does not exist")


def calculate_gpa(dict:dict, id: str)->float:
    """Calculates a students GPA based on their results"""
    id: str # student ID
    grade_points: int # grade points earned
    
    if check_id(dict, id):
        grade_points = 0
        for i in range(len(dict[id])):
            if dict[id][i] >= 80:
                grade_points += 7
            elif dict[id][i] >= 70:
                grade_points += 6
            elif dict[id][i] >= 60:
                grade_points += 5
            elif dict[id][i] >= 50:
                grade_points += 4
            else:
                grade_points += 0
        gpa = grade_points / len(dict[id])
        print(f'GPA of student {id}: {gpa}')
        return gpa
    else:
        print("Student does not exist")


def main():
    students = {}
    choice = 0 # Variable to hold user's choice
    
    
    SID_PROMPT = "Enter the student ID: "
    
    print("Student GPA Calculator")
    while choice != 6:
        print()
        print("1. Add student\n"
              "2. Add result to existing student\n"
              "3. Calculate average\n"
              "4. Calculate GPA\n"
              "5. List students\n"
              "6. Quit\n")
        try:
            choice = int(input("Action: "))
            match choice:
                case 1:
                    add_student(students, str(input(SID_PROMPT)))
                case 2:
                    add_result_for_student(students, str(input(SID_PROMPT)))
                case 3:
                    calculate_average(students, str(input(SID_PROMPT)))
                case 4:
                    calculate_gpa(students, str(input(SID_PROMPT)))
                case 5:
                    display_students(students)
        except:
            print("Invalid input. ")
    print("Exiting program...")


if __name__ == "__main__":
    main()
