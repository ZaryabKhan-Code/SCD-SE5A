"""
Week 2 Demo: Basic Python code to refresh concepts such as data types, OOP, and more.
Run: python week2_python_basics.py
"""

# Simple class for demonstration
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

def main():
    # Data types
    my_list = [1, 2, 3]
    my_dict = {"course": "Flask", "semester": 5}
    print("List:", my_list)
    print("Dictionary:", my_dict)

    # OOP demonstration
    greeter = Greeter("Student")
    print(greeter.greet())

if __name__ == "__main__":
    main()
