class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

def main():
    stud1 = Student("John", 20)

    print("Example of class usage:")
    print("Student name: ", stud1.get_name())

if __name__ == "__main__":
    main()