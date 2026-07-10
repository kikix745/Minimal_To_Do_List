#To Do List



tasks=[]

def Show_Menu():
    print("-------To-Do List-------")
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark task as done")
    print("4.Delete task")
    print("5.Exit")
    print("------------------------")

    print("Choose option from the list (1-5)")

def Add_Task():
    task=input("Enter your task")
    tasks.append({"task":task,"Done":False})
    print(f"task:{task} added !")

def view_tasks():
    if not tasks:
        print("No tasks yet")
        return
    print("\nyour tasks ")   
    for index,task in enumerate(tasks,start=1):
        status="☑" if task["Done"] else"✘"
        print(f"{index}.{task["task"]} [{status}]")
    
def mark_Done():  
    view_tasks()
    if not tasks:
        return 
    try:
        index=int(input("enter the task you finished"))-1
        if 0<=index<len(tasks) :
            tasks[index]["Done"]=True
            print("the task is done")
        else:
            print("invalid number")   
    except ValueError:
        print("enter real number")           
       
def delete_task():
    view_tasks() 
    if not tasks:
        return 
    try:
        index=int(input("enter the task number delete"))-1
        if 0<=index<len(tasks) :
            removed_task=tasks.pop(index)
            print(f"deleted task:{ removed_task['task']}")
        else:
            print("invalid number")   
    except ValueError:
        print("enter real number")
    
    
while True:
        Show_Menu()
        choice=input("enter you choice :")
        if (choice=='1'):
             Add_Task()
        elif (choice=='2'):
            view_tasks()
        elif (choice=='3'):
            mark_Done()
        elif (choice=='4'): 
             delete_task()  
        elif (choice=='5'): 
            print("GoodBye Mate!")
            break
        else:
            print("invalid choice try again")    
             
        
        
