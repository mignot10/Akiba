def calculate_grade(students,Passing_score):
    if not students:
        return "No students provided."
    for student in students:
        if 'name' not in student or 'score' not in student or student['score'] < 0:
            print("Each student must have a non-negative 'score'.")
            return "Invalid student data."
        if 90 <= student['score'] <= 100:
            student['grade'] = 'A'
        elif 80 <= student['score'] < 90:
            student['grade'] = 'B'
        elif 70 <= student['score'] < 80:
            student['grade'] = 'C'
        elif 60 <= student['score'] < 70:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'

    return {student['name']: student['grade'] for student in students if student['score'] >= Passing_score}

def calculate_average(students):
    if not students:
        return 0
    total_score = 0
    for student in students:
        if 'score' not in student or student['score'] < 0:
            print("Each student must have a non-negative 'score'.")
            return 0
        total_score += student['score']
    return total_score / len(students)

def largest_grades(students):
    if not students:
        return None
    largest = students[0]
    for student in students:
        if student["score"] > largest["score"]:
            largest = student
    return largest

def lowest_grade(students):
    if not students:
        return None
    lowest = students[0]
    for student in students:
            if student["score"] < lowest["score"]:
                lowest = student
    return lowest

def passed_students(students,passing_score):
    passed = []
    failed = []
    for student in students:
        if student["score"] >= passing_score:
            passed.append(student)
        else:
            failed.append(student)
    number_passed = len(passed)
    number_failed= len(failed)
    return number_failed,number_passed

def above_average_students(students):
    avg = calculate_average(students)
    return [student for student in students if student["score"] > avg]

def report_card(students,passing_score=50):
    if not students:
        print("No student data available")
        return

    #Assign grades first
    calculate_grade(students, passing_score)
    avg = calculate_average(students)
    highest = largest_grades(students)
    lowest = lowest_grade(students)
    num_failed, num_passed = passed_students(students, passing_score)
    above_avg = above_average_students(students)

    print("\n" + "="*40)
    print("      STUDENT PERFORMANCE REPORT      ")
    print("="*40)
    print(f"Class Average Score : {avg:.2f}")
    print(f"Highest Score       : {highest['name']} ({highest['score']})")
    print(f"Lowest Score        : {lowest['name']} ({lowest['score']})")
    print(f"Passed Students     : {num_passed}")
    print(f"Failed Students     : {num_failed}")

    print("\n--- Students Above Class Average ---")
    if above_avg:
        for s in above_avg:
            print(f"- {s['name']} (Score: {s['score']})")
    else:
        print("None")
    print("="*40)

if __name__ == "__main__":
    students = [
        {"name": "Sara", "score": 85},
        {"name": "Ahmed", "score": 42},
        {"name": "Musa", "score": 93},
        {"name": "Hana", "score": 67}
    ]

    report_card(students, passing_score=50)