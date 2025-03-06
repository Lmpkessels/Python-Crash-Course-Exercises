tasks = []

while True:
    #Display menu options
    print("\nMenu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delet a task")
    print("4. Exit")

#Get user's choice
choice = input("Enter you choice (1-4)")

if choice == "1":
    #Add a new task
    new_task = input("Add a new task: ")
    tasks.append(new_task) #Append the task to the list
    print("Task added successfully!")
elif choice == 2:
    #View tasks
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1): #Display tasks with numbers
            print(f"{i}. {task}")
            
elif choice == "3":
    #Delete a task
    if not tasks: #Check if the list is empty
        print("No tasks to delete.")
    else:
        print("nYour Tasks")
        for i, task in enumerate(tasks, start=1): #Display tasks with numbers
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks): #Check if the number is valid
                print(f"Task, '{deleted_task} deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
elif choice == "4":
    #Exit the program
    print("Goodbye!")
else:
    #Invalid input
    print("Invalid choice. Please try again.")