import datetime
import time
name=input("Enter Your Name::")
peresent= datetime.datetime.now().hour
if 3 <= peresent <= 12 :
    print("Good Morning☀️ " , name.upper())
elif 12 <= peresent <= 7:
    print("Good Afternoon🌇 " , name.upper()) 
else:
    print("Good Night⏾ " , name.upper())

print("       🙏NAMASTE🙏\n Wellcome To Chate Assistant") 
x="you can ask me question's regarding python programing\ntype 'BYE' to exit"
print(x.title())
# pyhton memory
python_knowledge = {
    "hello":"wellcome How Can i Help You",
    # Chapter 1
    "what is programming": "Programming is giving instructions to a computer to perform a task. Example: print('Hello').",
    "what is python": "Python is an easy-to-learn, high-level programming language. Example: print('Hello World').",
    "features of python": "Python is easy, readable, open-source, portable, interpreted, and has many libraries.",
    "what is installation": "Installation means installing Python on your computer so you can write and run Python programs.",
    "first python program": "Example: print('Hello, World!')",
    "what is a module": "A module is a Python file containing reusable code. Example: import math.",
    "what is pip": "pip is Python's package manager. Example: pip install requests.",
    "built in vs external modules": "Built-in modules come with Python, while external modules are installed separately. Example: math is built-in and requests is external.",
    "what is repl": "REPL lets you run Python commands one at a time and immediately see the result. Example: >>> 2 + 3 gives 5.",
    "what are comments": "Comments are notes ignored by Python. Example: # This is a comment.",

    # Chapter 2
    "what is a variable": "A variable stores a value. Example: age = 20.",
    "what are data types": "Data types describe the kind of data. Common types include int, float, str, bool, list, tuple, dict, and set. Example: age = 20.",
    "what are identifiers": "Identifiers are names used for variables, functions, classes, etc. Example: student_name = 'Rahul'.",
    "what are operators": "Operators perform operations on values. Example: 5 + 3 gives 8.",
    "what is type": "type() tells you the data type of a value. Example: type(10) returns int.",
    "what is typecasting": "Typecasting converts one data type into another. Example: int('10') converts a string into an integer.",
    "what is input": "input() takes information from the user. Example: name = input('Enter your name: ').",

    # Chapter 3
    "what is a string": "A string is a sequence of characters inside quotes. Example: name = 'Python'.",
    "what is string indexing": "Indexing accesses a character using its position. Example: 'Python'[0] gives 'P'.",
    "what is string slicing": "Slicing extracts part of a string. Example: 'Python'[0:3] gives 'Pyt'.",
    "what is skip value": "The skip value controls how many positions Python moves while slicing. Example: 'Python'[0:6:2] gives 'Pto'.",
    "what are string functions": "String functions perform operations on strings. Example: 'python'.upper() gives 'PYTHON'.",
    "what are escape sequences": "Escape sequences represent special characters. Example: \\n creates a new line.",

    # Chapter 4
    "what is a list": "A list stores multiple values and can be changed. Example: numbers = [1, 2, 3].",
    "what is list indexing": "List indexing accesses an item using its position. Example: [10, 20, 30][0] gives 10.",
    "what are list methods": "List methods modify or work with lists. Example: numbers.append(4) adds 4 to a list.",
    "what is a tuple": "A tuple is an ordered collection that normally cannot be changed. Example: numbers = (1, 2, 3).",
    "what are tuple methods": "Tuple methods include count() and index(). Example: (1, 2, 2).count(2) gives 2.",

    # Chapter 5
    "what is a dictionary": "A dictionary stores data as key-value pairs. Example: student = {'name': 'Rahul'}.",
    "dictionary properties": "Dictionaries are mutable, use key-value pairs, and keys must be unique. Example: {'name': 'Rahul'}.",
    "what are dictionary methods": "Dictionary methods work with dictionary data. Example: student.get('name') returns the value of name.",
    "what is a set": "A set is a collection of unique values. Example: numbers = {1, 2, 3}.",
    "set properties": "Sets contain unique values and do not support normal indexing. Example: {1, 2, 2} becomes {1, 2}.",
    "set operations": "Sets support union, intersection, difference, and symmetric difference. Example: {1, 2} | {2, 3} gives {1, 2, 3}.",

    # Chapter 6
    "what is if": "if runs code when a condition is true. Example: if age >= 18: print('Adult').",
    "what is else": "else runs when the if condition is false. Example: if age >= 18: print('Adult') else: print('Minor').",
    "what is elif": "elif checks another condition when the previous condition was false. Example: elif age >= 13: print('Teen').",
    "what are relational operators": "Relational operators compare values. Example: 10 > 5 returns True.",
    "what are logical operators": "Logical operators combine conditions. They are and, or, and not. Example: age >= 18 and age <= 60.",

    # Chapter 7
    "what is a loop": "A loop repeats code. Python mainly uses for and while loops. Example: for i in range(3): print(i).",
    "what is while": "A while loop repeats while a condition is true. Example: while x < 5: x += 1.",
    "what is for": "A for loop repeats through a sequence. Example: for i in range(3): print(i).",
    "what is range": "range() generates a sequence of numbers. Example: range(5) produces 0 to 4.",
    "what is for else": "for...else runs the else block when the loop finishes normally. Example: for i in range(3): print(i) else: print('Done').",
    "what is break": "break immediately stops a loop. Example: if i == 3: break.",
    "what is continue": "continue skips the current loop iteration. Example: if i == 2: continue.",
    "what is pass": "pass does nothing and is used as a placeholder. Example: if True: pass.",

    # Chapter 8
    "what is a function": "A function is reusable code that performs a task. Example: def greet(): print('Hello').",
    "what is a function definition": "A function definition creates a function using def. Example: def add(a, b): return a + b.",
    "what is a function call": "A function call runs a function. Example: greet().",
    "what are arguments": "Arguments are values passed to a function. Example: greet('Rahul').",
    "what is a return value": "return sends a value back from a function. Example: return a + b.",
    "what are default parameters": "Default parameters have a value used when no argument is provided. Example: def greet(name='User'): print(name).",
    "what is recursion": "Recursion happens when a function calls itself. Example: a countdown function can call itself with n - 1.",

    # Chapter 9
    "what is file io": "File I/O means reading from and writing to files. Example: open('data.txt', 'r').",
    "text vs binary files": "Text files store readable characters, while binary files store binary data. Example: .txt is text and .jpg is binary.",
    "what is open": "open() opens a file. Example: file = open('data.txt', 'r').",
    "how to read a file": "Use read() to read file contents. Example: data = file.read().",
    "how to write a file": "Use write() to write data. Example: file.write('Hello').",
    "what are file modes": "Common file modes are r for reading, w for writing, and a for appending. Example: open('data.txt', 'w').",
    "what is with in file handling": "with automatically handles closing a file. Example: with open('data.txt') as file: data = file.read().",

    # Chapter 10
    "what is oop": "OOP means Object-Oriented Programming. It organizes programs using classes and objects.",
    "what is a class": "A class is a blueprint for creating objects. Example: class Student: pass.",
    "what is an object": "An object is an instance of a class. Example: student = Student().",
    "what are attributes": "Attributes are data belonging to a class or object. Example: self.name = 'Rahul'.",
    "what are methods": "Methods are functions defined inside a class. Example: def greet(self): print('Hello').",
    "what are class attributes": "Class attributes belong to the class and are commonly shared by its objects. Example: school = 'ABC School'.",
    "what are instance attributes": "Instance attributes belong to a particular object. Example: self.name = name.",
    "what is self": "self refers to the current object. Example: self.name = name.",
    "what is static method": "A static method does not require self. Example: @staticmethod def add(a, b): return a + b.",
    "what is init": "__init__() runs when an object is created and is commonly used to initialize its data. Example: def __init__(self, name): self.name = name.",

    # Chapter 11
    "what is inheritance": "Inheritance allows a child class to use properties and methods of a parent class. Example: class Dog(Animal): pass.",
    "what is single inheritance": "Single inheritance means one child class inherits from one parent class. Example: class Dog(Animal): pass.",
    "what is multiple inheritance": "Multiple inheritance means one class inherits from more than one parent class. Example: class C(A, B): pass.",
    "what is multilevel inheritance": "Multilevel inheritance forms a chain of inheritance. Example: Animal -> Mammal -> Dog.",
    "what is super": "super() is used to access a parent class method or constructor. Example: super().__init__().",
    "what is a class method": "A class method works with the class and uses cls. Example: @classmethod def change(cls): pass.",
    "what is property": "@property allows a method to be accessed like an attribute. Example: @property def name(self): return self._name.",
    "what are getters and setters": "A getter reads a value and a setter changes a value. Example: @property can be used to create them.",
    "what is operator overloading": "Operator overloading gives operators special behavior for objects. Example: __add__() can define how + works.",
    "what are dunder methods": "Dunder methods have double underscores and provide special behavior. Example: __str__() controls how an object is displayed.",

    # Chapter 12
    "what is walrus operator": "The walrus operator := assigns a value inside an expression. Example: if (n := len('Python')) > 5: print(n).",
    "what are type hints": "Type hints show the expected data type. Example: def add(a: int, b: int) -> int: return a + b.",
    "what are advanced type hints": "Advanced type hints include list[int], dict[str, int], tuple[int, str], and int | str. Example: names: list[str].",
    "what is match case": "match-case is used for pattern matching. Example: match day: case 1: print('Monday').",
    "what is dictionary merge": "Dictionaries can be merged using |. Example: {'a': 1} | {'b': 2}.",
    "what is exception handling": "Exception handling manages errors using try and except. Example: try: x = 10 / 0 except ZeroDivisionError: print('Error').",
    "what is raise": "raise manually creates an exception. Example: raise ValueError('Invalid value').",
    "what is try else": "The try else block runs else when no exception occurs. Example: try: x = 10 / 2 except: pass else: print('Success').",
    "what is finally": "finally runs whether an exception occurs or not. Example: try: print('Hi') finally: print('Done').",
    "what is name main": "__name__ == '__main__' checks whether a Python file is being run directly. Example: if __name__ == '__main__': main().",
    "what is global": "global allows a function to modify a global variable. Example: global x.",
    "what is enumerate": "enumerate() gives both the index and value while looping. Example: for i, name in enumerate(names): print(i, name).",
    "what are list comprehensions": "List comprehensions create lists in a short way. Example: squares = [x*x for x in range(5)].",
    "bye": "Thank You For Using Me,Have A Nice Day..👋"
}
# function
def get_respone_of_BOT(userQUESTION):
    userQUESTION=userQUESTION.lower()
    for eachkey in python_knowledge: #purpsoe to cheak the key in dictnory
        if eachkey in userQUESTION: # cheak matching ans 
            return python_knowledge[eachkey]
    return "I am not able to Answer,Still In Learning Mode..⚙️"   
     



# user input
while True:
    USERINPUT= input("Ask Your Question::")
    REPLY= get_respone_of_BOT(USERINPUT)
    print("ANSWER:",REPLY)

    if "bye" in USERINPUT.lower():
        break
