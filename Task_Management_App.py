
tasks = [] # empty list
print("---------WELCOME TO THE TASK MANAGEMENT APP---------")
    
total_task = int(input("Enter how many task you want to add = "))
for i in range(1,total_task+1): #6
        task_name = input(f"Enter task {i} = ").lower()
        tasks.append(task_name)
        
print(f"\n Today's task are = {tasks}\n")
        
while True:
        operation = int(input("Operations : \n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Stop\n Enter Your Choice : "))
        if operation == 1:
            add = input("Enter task you want to add = ").lower()
            tasks.append(add)
            print(f"Task {add} has been successfully added.....\n")
            
        elif operation == 2:
            update_val = input("Enter the task name you want to update = ").lower()
            if update_val in tasks:
                up = input("Enter new task = ").lower()
                if update_val != up:
                  indx = tasks.index(update_val)
                  tasks[indx] = up
                  print(f"Task has been successfully updated.....\n")
                else:
                    print("TasK already exist...\n")
            else:
                print(f"'{update_val}' is not exist.....\n")
                
        elif operation == 3:
            del_val = input("Which task you want to delete = ").lower()
            if del_val in tasks:
                indx = tasks.index(del_val)
                del tasks[indx]
                print(f"Task '{del_val}' has been deleted....\n")
                
        elif operation == 4:
            print(f"Total tasks = {tasks}\n")
            
        elif operation == 5:
            print("Closing the program....Visit again!")
            break
        else:
            print("Invalid Choice...")
            

          
        
        