'''
Todo app-Assignment of DeeploAI w3--
A user can add tasks to the todo list.

User can set a due date to this task

user can check a task completed or not

if the task is not completed, show in incomplete tasks.

Also, user can complete the task.

Users can set a priority for this task. (You can do either important, not important or set a level like 0-5)

User can delete this task form list

So basically this task has a few features like due date, completed status and priority.
'''



import time

todo_dict={
        1:{'Task_Name':'loginsystem','Due_Date':'10-10-2019','Priority':3, 'Status':'Completed'},
        2:{'Task_Name':'todoapp','Due_Date':'12-10-2019','Priority':3, 'Status':'Continue'}         
          }
print('WELCOME TO TODO APP\nYou can add/change/check your tasks here...\n')
time.sleep(1) # Wait for 1 seconds

def task_list():
    print('Your Current Task List:')
    print('No\tTask Name\tDue Date\tPriority\tStatus')
    global todo_dict
    dict_index=list(range(1,len(todo_dict)+1))
    todo_dict = dict(zip(dict_index, list(todo_dict.values())))
    for n in range(1,len(todo_dict)+1):
        task_detail=todo_dict[n]
        task_name=task_detail.get('Task_Name')
        task_duedate=task_detail.get('Due_Date')
        task_priority=task_detail.get('Priority')
        task_status=task_detail.get('Status')    
        print('{} \t{} \t{} \t{}\t\t{}'.format(n,task_name,task_duedate,task_priority,task_status))
    print()
    task_action()

def task_action():
    while True:
        question_task=input("What do you want to do?\n'Add a New Task', 'Delete a Task', 'Update a Task', 'Exit'\nYou can enter 'add','delete','update','exit' or 1,2,3,4\n").lower()
        if question_task=='add new task' or question_task=='add' or question_task=='1':
            task_add()
            break
        elif question_task=='delete a task' or question_task=='delete' or question_task=='2':
            task_del()
            break
        elif question_task=='update a task' or question_task=='update' or question_task=='3':
            task_update()
            break
        elif question_task=='exit' or question_task=='4':
            exit()
            break
        else:
            print("\nPlease only enter 'add','delete','update','exit' or 1,2,3,4")
            
def task_add():
    print('You can add a new task with the instructions')
    m=len(todo_dict)
    task_name=input('Set a username:\n')
    task_duedate=input('Set the Due Date in D-M-Y Format:\n')    
    while True:
        task_priority=input('Set the Priority in 1 to 5:\n')
        if task_priority.isdigit()==True:
            task_priority=int(task_priority)
            if task_priority in range(1,6):
                break
            else:
                print('Please set a value between 1 to 5')
        else:
            print('Please set a value between 1 to 5')
    task_status=input('Set the Status: (ex:Completed,Continue)\n')
    todo_dict[m+1]={'Task_Name':task_name,'Due_Date':task_duedate,'Priority':task_priority,'Status':task_status}
    print('New task adding to list successfully!')
    exit()
    
def task_update():
    print('You can update your existing tasks with the instructions')
    m=len(todo_dict)
    while True:
        question_del=input('Please enter the task number, which you want to update? Between 1 to {}\n'.format(m)).lower()
        if question_del.isdigit()==True:
            question_del=int(question_del)
            if question_del in range(1,m+1):
                while True:
                    question_del_detail=input("Do you want to change the Task Name of '{}''? Yes or No?\n".format(todo_dict[question_del]['Task_Name'])).lower()
                    if question_del_detail == "yes" or question_del_detail == "y":
                        new_taskname=input("Please write the new Task Name for '{}'".format(todo_dict[question_del]['Task_Name']))                  
                        todo_dict[question_del]['Task_Name']=new_taskname
                        print('New task name updated successfully!')
                        break
                    elif question_del_detail == "no" or question_del_detail == "n":
                        break
                    else:
                        print("Please only enter yes or no")
                while True:
                    question_del_detail=input("Do you want to change the Status of '{}''? Yes or No?\n".format(todo_dict[question_del]['Task_Name']))
                    if question_del_detail == "yes" or question_del_detail == "y":
                        new_statusname=input("Please write the new Status for '{}'(ex:Completed,Continue)".format(todo_dict[question_del]['Task_Name']))                 
                        todo_dict[question_del]['Status']=new_statusname
                        print('New task status updated successfully!')
                        exit()
                        break
                    elif question_del_detail == "no" or question_del_detail == "n":
                        exit()
                        break
                    else:
                        print("Please only enter yes or no")
                break

            else:
                print("Please set a value between 1 to {}".format(m))
        else:
            print("Please set a value between 1 to {}".format(m))
    
def task_del():
    print('You can delete your existing tasks with the instructions')
    m=len(todo_dict)
    while True:
        question_del=input('Please enter the task number, which you want to delete? Between 1 to {}\n'.format(m)).lower()
        if question_del.isdigit()==True:
            question_del=int(question_del)
            if question_del in range(1,m+1):
                todo_dict.pop(question_del)
                print('The selecting task successfully deleted')
                task_list()
                break
            else:
                print("Please set a value between 1 to {}".format(m))
        else:
            print("Please set a value between 1 to {}".format(m))  
    
def exit():
    while True:
        question_exit=input('Do you want to exit? Yes or No?\n').lower()
        if question_exit== "yes" or question_exit== "y":
            print("You are successfully logged out")
            break
        if question_exit== "no" or question_exit== "n":
            task_list()
            break
        else:
            print("Please only enter yes or no")

task_list()