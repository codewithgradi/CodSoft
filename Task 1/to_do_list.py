import csv
import sys

tasks = []

def main():
    load_task()
    while True:
        print("===============================")
        print("++++++ TO DO LIST +++++++++")
        print("===============================")
        print("1. VIEW ALL TASKS")
        print("2. MARK TASK COMPLETE")
        print("3. REMOVE TASK")
        print("4. VIEW UNCOMPLETED TASKS")
        print("5. ADD NEW TASK")
        print("6. MARK TASK UN-COMPLETED")
        print("7. Exit")
        print("8. View Completed Tasks")
        print("===============================")
        action = input("What do you want to do? Eg.1 to see all tasks\t")
        if action=="1":
            track_all_tasks()
        elif action=="2":
            id_to_update=input("Enter task ID of task to be updated: \t")
            completed(id_to_update)
        elif action=="3":
            task_id=input("Enter the task ID of TASK to be REMOVED\t")
            remove_task(task_id)
        elif action=="4":
            view_un_completed()
        elif action=="5":
            id = input("Enter ID of new task\n")
            task = input("What is the task?\n")
            add_task(id,task)
        elif action=="6":
            id = input("Enter task ID of task to update status to 'un-completed'")
            mark_uncomplete(id)
        elif action=="7":
            sys.exit()
        elif action=="8":
            view_complted_tasks()
        
        else:
            print("Inavlid Input")
        
def add_task(id:str,task:str,status="un-completed"):
    #checks if task details are added
    if (id!="") and (task!="") and (status!=""):
        newtask = {"id":id,"task":task,"status":status}
        tasks.append(newtask)
        print("TASK ADDED SUCCESSFULLY")
        write_new_data()
        
    else:
        print("TASKS CAN NOT BE ADDED")    

def track_all_tasks():
    print("++++++++++++++ALL TASKS ++++++++++++++++++++++++++++++++++++")
    print("Task ID\t\tTask\t\t\tStatus")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for task in tasks:
        print(f"|{task['id']}|\t\t|{task['task']}|\t\t|{task['status']}|")
        print("------------------------------------------------------------")
def view_un_completed():
    print("++++++++++++++TASKS THAT YOU NEED TO COMPLETE ++++++++++++++++++++++++++++++++++++")
    print("Task ID\t\tTask\t\t\tStatus")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for task in tasks:
        if task['status']=="un-completed":
            print(f"|{task['id']}|\t\t|{task['task']}|\t\t|{task['status']}|")
            print("------------------------------------------------------------")
def completed(task_id:str):

    found =False

    for task in tasks:
        if task_id==task['id']:
            task['status']="completed"
            found=True
            break

    if not found:
        print(f"Could not find task with task id {task_id}")

    if found:
        print()
        write_new_data()

def write_new_data():
    with open("Tasks.csv","w",newline="")as file:
        fieldnames=tasks[0].keys()
        line = csv.DictWriter(file,fieldnames=fieldnames)
        line.writeheader()
        line.writerows(tasks)
    print()
    print("DATE HAS BEEN UPDATED")

def remove_task(task_id:str):
    #boolean variable used to check if task id entered by user is valid
    found=False
    #loops through tasks list
    for task in tasks:
        if task_id==task["id"]:
            found = True
            print(f"|{task["id"]}|\t|{task["task"]}|\t|{task["status"]}|\t|HAS BEEN REMOVED")
            #removes task from list
            tasks.remove(task)
            break
    
    #writes new data on 
    if found:
        write_new_data()

    #executes if task id is inavlid
    if not found:
        print("Invalid Task ID: Task ID was not found!")

def mark_uncomplete(task_id:str):
    found =False

    for task in tasks:
        if task_id==task['id']:
            task['status']="un-completed"
            found=True
            break

    if not found:
        print(f"Could not find task with task id {task_id}")

    if found:
        print()
        write_new_data()

def view_complted_tasks():
    print("++++++++++++++TASKS THAT YOU HAVE COMPLETED ++++++++++++++++++++++++++++++++++++")
    print("Task ID\t\tTask\t\t\tStatus")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for task in tasks:
        if task['status']=="completed":
            print(f"|{task['id']}|\t\t|{task['task']}|\t\t|{task['status']}|")
            print("------------------------------------------------------------")


#loads tasks from textfile into a dictionary then dictionaries into list called tasks
def load_task():
    with open("Tasks.csv","r")as file:
        content_data= csv.DictReader(file)
        for line in content_data:
            tasks.append(line)

if __name__=='__main__':
    main()



