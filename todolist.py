tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        # get task from user and append to list
        user=input("enter task: ")
        tasks.append(user)       
    elif choice == "2":
        # print all tasks
        
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        
    elif choice == "3":
        # remove a task
        remove=input("enter del task:")
        tasks.remove(remove)
        
    elif choice == "4":
        # stop the loop
        break