RED = "\033[31m"
ORANGE = "\033[38;2;255;165;0m"
RESET = "\033[0m"
FILENAME = "tasks.txt"

menu = """1 - Add a task
2 - View my to-do list
3 - Mark task as completed
4 - Remove a task
5 - Quit
"""

def loadTasks():
    pending, done = [], []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[DONE] "):
                    done.append(line[7:])
                elif line:
                    pending.append(line)
    except FileNotFoundError:
        pass
    return pending, done

def saveTasks():
    with open(FILENAME, "w") as f:
        for task in taskPending:
            f.write(task + "\n")
        for task in taskDone:
            f.write("[DONE] " + task + "\n")

taskPending, taskDone = loadTasks()

def addTask():
    task = input(RED + "What are we going to do, Champ? " + RESET).strip()
    if not task: #checking blank tasks
        print(RED + "Can't add an empty task, Champ!" + RESET)
        print(ORANGE + "=" * 30 + RESET + "\n")
        return
    taskPending.append(task) #adding task to Pending list
    print(RED + "Task is successfully added!" + RESET)
    saveTasks()
    print(ORANGE + "=" * 30 + RESET + "\n")

def viewTask():
    if taskPending:
        print(RED + "===TASKS PENDING===" + RESET)
        for i in taskPending: #printing Pending list
            print(i)
        print()

    if taskDone:
        print(RED + "====TASKS DONE====" + RESET)
        for i in taskDone: #printing Done list
            print(i)
        print()

    if not taskPending and not taskDone: #Checks if both Lists are clear
        print(RED + "Nothing here yet, Champ!" + RESET)

    print(ORANGE+ "=" * 30 + RESET + "\n")

def markTask():
    if len(taskPending) == 0: #Checks if Pending list has tasks
        print(RED + "All done, Champ!" + RESET)
        print(ORANGE + "=" * 30 + RESET + "\n")
        return
    
    if taskPending: 
        for i,task in enumerate(taskPending): #Printing tasks numbered
            print(f"{i+1} - {task}")
        print()
            
    taskNumber = getValidTaskNumber(taskPending)

    taskDone.append(taskPending.pop(taskNumber - 1)) #Switching task status from Pending to Done
    saveTasks()
    print(ORANGE + "=" * 30 + RESET + "\n")

def removeTask():
    if len(taskPending) == 0: #Checks if Pending list has tasks
        print(RED + "Nothing to remove!" + RESET)
        print(ORANGE + "=" * 30 + RESET + "\n")
        return
    
    else:
        for i,task in enumerate(taskPending): #Printing tasks numbered
                    print(f"{i+1} - {task}")
        print()

    taskNumber = getValidTaskNumber(taskPending)

    taskPending.pop(taskNumber - 1) #Removing task from the list
    print(RED + "Task is successfully removed!" + RESET)
    saveTasks()
    print(ORANGE + "=" * 30 + RESET + "\n")

def getValidTaskNumber(taskList):
    while True:
        num = input(RED + "Which task, Champ? " + RESET)
        if num.isdigit() and 1 <= int(num) <= len(taskList): #Checks if input is Digit && Digit < TasksCount
            return int(num)
        print(RED + "Invalid choice, try again." + RESET)

print(RED + "==WELCOME BACK TO THE WORK, CHAMP==" + RESET + "\n")
while True:
    print(menu)
    choice = input(RED + "What's the move, Champ: " + RESET)
    print()

    if choice == "1":
        addTask()
    elif choice == "2":
        viewTask()
    elif choice == "3":
        markTask()
    elif choice == "4":
        removeTask()
    elif choice == "5":
        print(RED + "See you soon, Champ!" +RESET)
        break
    else:
        print(RED + "Wrong input try again!" + RESET + "\n")