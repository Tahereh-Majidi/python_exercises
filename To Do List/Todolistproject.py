def add():
  task=input("Enter your task to add:  ")
  if task not in tasks:
    tasks.append(task)
    status.append(False)
    print("your task has been successfuly added \n")
  else:
            print(f"{task}: exist \n")
def display():
  for i, t in enumerate(tasks):
        flag="undone"
        if status[i]:
            flag="done"
        print(f"task_{i+1}: {t}---->{flag}")
def  edit():
 index=input("index of task: ")
 list1=[int(i)-1 for i in index.split()]
 for i in list1:
    new_task=input("new task: ")
    if new_task not in tasks:
        tasks[i]=new_task
    else:
      print(f"{new_task}: exist")
def  done(): 
   index=input("index of task: ")
   list1=[int(i)-1 for  i in index.split()]
   for i in list1:
            status[i]=True
def  remove():               
   index=input("index of task: ")
   list1=[tasks[int(i)-1] for  i in index.split()]
   for t in list1:
           i=tasks.index(t)
           tasks.pop(i)
           status.pop(i)
def search ():
     word=input("task to search:  ")
     for i, t in enumerate(tasks):
            if word in t:
                flag="undone"   
                if status[i]:
                    flag="done"
                print(f" {t}---->{flag}")
#_________________________main_______________________

tasks=[]  #string
status=[]  #boolean
#add , remove, edit, search
while True:
    user=input("To-DO List>>> Select one option(add/remove/edit/search/display):")
    if user=="add":
        add()
        display()
    elif  user=="display":
        #task_1: python ----> done
        #True---->done, False---->undone
        display()
    elif user=="edit":
            edit()
            display()
    elif user=="done":
           done()
           display()
    elif user=="remove":
         remove()
         display()
    elif user=="search":   
        search ()
    elif user=="":
        pass
    elif user=="exit":
        break
    else:
        print(f"{user}: command not found!")
