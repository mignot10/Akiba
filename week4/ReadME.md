# Week 4 Python Task: Mutability, References, and Memory Model

---

## Assignment Overview & Theoretical Answers

### Question 1: Mutable and Immutable Objects
* **Mutable objects** (e.g., `list`, `dict`, `set`) can be altered in place after creation without changing their memory address.
* **Immutable objects** (e.g., `int`, `float`, `str`, `tuple`) cannot be changed after creation. Any modification results in a brand-new object being created in memory.

### Question 2: References and Object Identity
* **`is` operator**: Checks object identity (whether two variables point to the exact same object in memory).
* **`==` operator**: Checks value equality (whether the contents of two objects are equal).
* `a` and `c` have equal values (`==` is True) because they contain identical items, but different identities (`is` is False) because they occupy distinct spaces in memory.

### Question 3: Shared References and Side Effects
* When assigning `values = numbers`, both variables reference the exact same underlying list object. Modifying one via `.append()` alters the shared object, creating side effects on the other. 
* To prevent this, use `.copy()` or list slicing `[:]` to create a shallow copy.

### Question 4: Function Arguments and Mutability
* When a mutable object like a list is passed into a function, Python passes it by assignment reference. Modifications inside the function directly affect the caller's variable.
* To prevent mutation, pass a copy of the list or have the function construct and return a new list.

### Question 5: Memory Management and Garbage Collection
* Python manages memory automatically using private heaps and reference counting. When an object's reference count drops to zero (e.g., using `del` on all variables referencing it), Python's garbage collector frees its memory.
* Deleting a single reference (`del x`) reduces the reference count by 1, but does not destroy the object if other variables (like `y`) still reference it.

---

## Practical Mini-Project: Student Marks Manager

### Expected Program Output
```text
Original marks: [75, 80, 65, 90, 85]
Shared reference: [75, 80, 65, 90, 85]
Copied marks: [75, 80, 65, 90, 85, 95]

Original and shared reference are identical: True
Original and copied lists have equal values: False
Original and copied lists are identical: False