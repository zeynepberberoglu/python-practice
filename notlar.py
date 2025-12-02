# Core Python Concepts and Notes

# This is a comment line
# print("Hello World!")

# Data Input from User
# user_name = input("What is your name? ")

## --- Fundamental Data Types ---
x = 5               # int (Integer)
y = 3.14            # float (Floating-point number)
name = "Zeynep"     # str (String - text)
is_active = True    # bool (Boolean - True/False)

# Type Casting (Conversion)
age = int("19")     # Converts string "19" to integer 19
text_num = str(42)  # Converts integer 42 to string "42"

# String Operations
full_name = "Zeynep"
print(full_name.upper())    # Output: ZEYNEP (Converts to uppercase)
print(full_name[0:3])       # Output: Zey (Slicing: Start index is inclusive, end index is exclusive)
print(f"Hello {full_name}") # Formatted string (f-string)

## --- Operators ---
# Arithmetic: + - * / // (floor division) % (modulus) ** (exponentiation)
# Comparison: == != > < >= <=
# Logical: and or not
# Membership: "a" in "zeynep" # False

## --- Control Flow ---
# if-elif-else
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

# for Loop (Iteration)
# Iterates through numbers 0, 1, 2, 3, 4. Useful for performing the same operation 
# on all elements in a sequence (list, range, etc.)
for i in range(5):
    print(i)

# while Loop (Condition-based iteration)
counter = 0
while counter < 3:
    print("Hello")
    counter += 1

## --- Functions ---
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(2, 3))

# Default Parameters
def greet(name="Zeynep"):
    """Greets the user. Uses the default name if no parameter is provided."""
    print(f"Hello {name}!")
# If the user provides an argument, it is used; otherwise, "Zeynep" is used.

# Lambda Functions (Short, simple, anonymous function definitions)
square = lambda x: x ** 2 # x is the parameter, x ** 2 is the expression to be returned
print(square(5))    # 25

## --- Collections (Data Structures) ---

# Lists - Mutable (Changeable)
my_list = [1, 2, 3]
my_list.append(4)   # Adds 4 to the end
my_list.remove(2)   # Removes the first occurrence of 2
print(len(my_list)) # Returns the number of elements

# Tuples - Immutable (Unchangeable)
colors = ("red", "blue", "green")
# colors.append("yellow") # Error (Cannot modify immutable type)
# colors.remove("blue")   # Error (Cannot modify immutable type)

# Sets - Mutable but Unordered (No index)
# Each value is unique; duplicates are not allowed.
numbers = {1, 2, 3}

# Dictionaries - Key-Value pairs (Mapping)
student = {"name": "Zeynep", "age": 19}
print(student["name"])

## --- Exception Handling (try-except-finally) ---
try:
    # Code block where an error is anticipated
    num = int(input("Enter a number: "))
except ValueError:
    # Executed if a ValueError occurs (e.g., non-numeric input)
    print("Invalid input!")
else:
    # Executed only if no exception occurs in the 'try' block
    print("No error, operation successful.")
finally:
    # Executed regardless of whether an exception occurred or not
    print("Finished.")

## --- File Operations ---

# Opening a file (Absolute vs. Relative Path)
# file_r = open("data.txt", "r") # Relative path (if file is in the same directory)
# file_abs = open("C:/Users/Zeynep/Desktop/data/data.txt", "r") # Absolute path

# Read operation
try:
    file_read = open("deneme.txt", "r")
    content = file_read.read()
    print(content)
finally:
    file_read.close() # Always close the file to release system resources

# Write operation (Mode 'w' - overwrites file contents)
# file_write = open("deneme.txt", "w")
# file_write.write("Hello Zeynep!\n") # Wipes the file clean and writes new text
# file_write.write("I am learning Python :)\n")
# file_write.close()

# Append operation (Mode 'a' - adds to the end)
# file_append = open("deneme.txt", "a")
# file_append.write("This line was appended to the end.\n") # Adds without deleting existing content
# file_append.close()

# Recommended way: Using 'with' statement
# The file is automatically closed when the 'with' block finishes, even if errors occur.
with open("deneme.txt", "r") as file_handle:
    content = file_handle.read()
    print(content)

# File Modes
# r: Read only
# w: Write only (overwrites existing file)
# a: Append (adds to the end of existing file)
# x: Exclusive creation (creates a new file, fails if file already exists)

## --- Object-Oriented Programming (OOP) ---

class Car:
    # Constructor: Called automatically when a class object is created
    def __init__(self, brand, model):
        # self: Represents the instance (object) being created from the class
        self.brand = brand
        self.model = model

    def get_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car1.get_info()

# Inheritance
class ElectricCar(Car): # ElectricCar inherits properties from the Car class (Parent)
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model) # Calls the parent (Car) class's __init__ function
        self.battery_capacity = battery_capacity # Adds a specific attribute for ElectricCar

# Key OOP Concepts
# Encapsulation: Bundling data (attributes) and methods that operate on the data into a single unit (class).
# Inheritance: A class deriving properties and behaviors from another class.
# Polymorphism: The ability of a method (function) to behave differently based on the object it is called on.
# Abstraction: Hiding the complex implementation details and showing only the essential features.
