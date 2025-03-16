"""


 Task Manager App
 
 
 """



def task():
    tasks = []
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")

    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ").strip()
        tasks.append(task_name)

    print(f"\nToday's tasks: {tasks}\n")

    while True:
        try:
            operation = int(input("\nChoose an operation:\n"
                                  "1 - Add Task\n"
                                  "2 - Update Task\n"
                                  "3 - Delete Task\n"
                                  "4 - View Tasks\n"
                                  "5 - Exit\n"
                                  "Enter your choice: "))

            if operation == 1:
                add = input("Enter the task you want to add: ").strip()
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update: ").strip()

                if updated_val in tasks:
                    up = input("Enter new task: ").strip()
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Task '{updated_val}' updated to '{up}'.")
                else:
                    print("Task not found.")

            elif operation == 3:
                del_val = input("Enter the task name you want to delete: ").strip()

                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' has been successfully deleted.")
                else:
                    print("Task not found.")

            elif operation == 4:
                print(f"\nCurrent tasks: {tasks}")

            elif operation == 5:
                print("Closing the program. Have a great day!")
                break

            else:
                print("Invalid input, please enter a number between 1-5.")

        except ValueError:
            print("Please enter a valid number.")

task()
