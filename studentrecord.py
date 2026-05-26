class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

students = []

while True:
    print("1. Add students")
    print("2. View students")
    print("3. Remove student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        s = Student(name, marks)  # create object
        students.append(s)         # append object not just name       
    
    elif choice == "2":
        if len(students) == 0:
            print("No students yet!")
        else:
            for i, s in enumerate(students, 1):
                print(f"{i}.", end=" ")
                s.display()  # call display on each object!!
        
    elif choice == "3":
        # remove a task
        remove=input("enter del task:")
        students.remove(remove)
        
    elif choice == "4":
        # stop the loop
        break
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