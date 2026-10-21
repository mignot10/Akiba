# ==========================================
# Question 1: Mutable and Immutable Objects
# ==========================================
def demonstrate_mutability():
    print("--- Question 1: Mutable vs Immutable ---")
    # Demonstrating an immutable object (string)
    my_string = "hello"
    print(f"Original string: {my_string}, id: {id(my_string)}")  
    try: 
        my_string[0] = 'J'  # Raises TypeError because strings are immutable
    except TypeError as e:
        print(f"String modification failed as expected: {e}")

    # Create a new string instead of modifying the original
    my_string = "H" + my_string[1:]
    print(f"Modified string:{my_string}, id: {id(my_string)}")  # Reassigning the variable creates a new object in memory


    # Mutable object (list)
    my_list = [1, 2, 3]
    print(f"\nOriginal list: {my_list}, id: {id(my_list)}")
    my_list[0] = 10  # Modifies the list in place without changing its memory address id
    print(f"Modified list: {my_list}, id: {id(my_list)}")

# ==========================================
# Question 2: References and Object Identity
# ==========================================
def explain_identity():
    print("\n--- Question 2: References & Identity ---")
    a = [10, 20, 30]
    b = a
    c = [10, 20, 30]

    print("a is b:", a is b)    # True (b points to the exact same object as a)
    print("a is c:", a is c)    # False (c is a separate object created in memory)
    print("a == c:", a == c)    # True (a and c contain equal values)

# ==========================================
# Question 3: Shared References & Side Effects
# ==========================================
def demonstrate_shared_reference():
    print("\n--- Question 3: Shared References ---")
    numbers = [1, 2, 3]
    values = numbers
    values.append(4)
    print("numbers:", numbers)  # Output will show [1, 2, 3, 4]
    print("values:", values)    # Output will show [1, 2, 3, 4]

    # Preventing side effects by creating an independent copy
    original = [1, 2, 3]
    safe_copy = original.copy()
    safe_copy.append(4)
    print("\nAfter using .copy():")
    print("Original untouched:", original)   # Output will show [1, 2, 3]
    print("Safe copy modified:", safe_copy)  # Output will show [1, 2, 3, 4]

# ==========================================
# Question 4: Function Arguments & Mutability
# ==========================================
def update_list(items):
    items.append(100)

def safe_update_list(items):
    return items + [100]  # Returns a brand new list object

def demonstrate_function_mutability():
    print("\n--- Question 4: Function Arguments ---")
    scores = [50, 60, 70]
    update_list(scores)
    print("Scores after mutating function:", scores) # Expected output: Scores after mutating function: [50, 60, 70, 100]

    base_scores = [50, 60, 70]
    new_scores = safe_update_list(base_scores)
    print("Base scores untouched:", base_scores)   # Expected output: Base scores untouched: [50, 60, 70]
    print("New scores returned:", new_scores)      # Expected output: New scores returned: [50, 60, 70, 100]

# ==========================================
# Question 5: Memory & Garbage Collection
# ==========================================
def demonstrate_garbage_collection():
    print("\n--- Question 5: Memory Management ---")
    x = [1, 2, 3]
    y = x
    print("Created list x, assigned to y.")
    del x
    print("Variable reference x deleted using del.")
    print("Object still exists in memory via y:", y)


if __name__ == "__main__":
    demonstrate_mutability()
    explain_identity()
    demonstrate_shared_reference()
    demonstrate_function_mutability()
    demonstrate_garbage_collection()