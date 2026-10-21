# week-4-python-task: student_marks_manager.py

def main():
    # 1. Create a list containing at least five student marks.
    original_marks = [75, 80, 65, 90, 85]
    
    # 2. Assign the original list to a second variable to demonstrate shared references.
    shared_reference = original_marks
    
    # 3. Create an independent copy of the original list.
    copied_marks = original_marks.copy()
    
    # 4. Add a new mark to the copied list without changing the original list.
    copied_marks.append(95)
    
    # 5. Display the original list, shared reference, and copied list.
    print(f"Original marks: {original_marks}")
    print(f"Shared reference: {shared_reference}")
    print(f"Copied marks: {copied_marks}\n")
    
    # 6. Use is and == to compare the original list with the shared reference and the copied list.
    print(f"Original and shared reference are identical: {original_marks is shared_reference}")
    print(f"Original and copied lists have equal values: {original_marks == copied_marks}")
    print(f"Original and copied lists are identical: {original_marks is copied_marks}")

if __name__ == "__main__":
    main()