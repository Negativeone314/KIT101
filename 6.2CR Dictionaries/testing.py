"""
6.2CR Dictionaries (Student GPA Calculator)
"""

__author__ = "Thomas Couser"

def check_student(stud_results: dict[str, list[int]], sid: str):
    ...

def add_student(stud_results: dict[str, list[int]], sid: str, result: int):
    """
    Adds a new student ID.
    """
    # TODO: Implement this function
    results = []
    results.append(result)
    stud_results[sid] = results
    
    ...


def add_result_for_student(stud_results: dict[str, list[int]], sid: str, result: int):
    """
    Adds a result to the results on record for an existing student.
    """
    # TODO: Implement this function
    ...


def list_students(stud_results: dict[str, list[int]]):
    """
    Displays all students and their results.
    """
    print(f"Displaying students and results for {len(stud_results)} record(s):")
    for k, v in stud_results.items():
        print(f"Results for {k}: {v}")

def calculate_average(sid: str):
    ...

def main():
    results: dict[str, list[int]] = {} # collection of students and unit results
    sid: str # student ID
    res: int # result in the range 0-100
    choice: int = 0 # user's menu selection
    
    grade_boundaries = {
        "HD" : 80, #High Distinction
        "DN" : 70, #Distinction
        "CR" : 60, #Credit
        "PP" : 50, #Pass
        "NN" : 0 #Fail
    }
    
    stud_results = {}

    SID_PROMPT = "Enter the student ID: "
    RES_PROMPT = "Enter a unit result between 0-100: "

    print("Student GPA Calculator")
    while choice != 6:
        print()
        print("1. Add student\n"
              "2. Add result to existing student\n"
              "3. Calculate average\n"
              "4. Calculate GPA\n"
              "5. List students\n"
              "6. Quit")
        choice = int(input("Action: "))
        match choice:
            case 1:
                # TODO: Add code here
                sid = input(SID_PROMPT)
                result = int(input(RES_PROMPT))
                add_student(stud_results, sid, result)
                print(stud_results)
                ...
            case 2:
                # TODO: Add code here
                ...
            case 3:
                # TODO: Add code here
                ...
            case 4:
                # TODO: Add code here
                ...
            case 5:
                list_students(results)


if __name__ == "__main__":
    main()
