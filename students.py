class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

def save_to_file(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.name},{s.marks}\n")

def load_from_file():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                students.append(Student(name, int(marks)))
    except FileNotFoundError:
        pass
    return students

# Load students when program starts
students = load_from_file()

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        s = Student(name, marks)
        students.append(s)
        save_to_file(students)  # save immediately!!
        print("Student added and saved!!")
    
    elif choice == "2":
        if len(students) == 0:
            print("No students yet!")
        else:
            for i, s in enumerate(students, 1):
                print(f"{i}.", end=" ")
                s.display()
    
    elif choice == "3":
        print("session over!!")
        break