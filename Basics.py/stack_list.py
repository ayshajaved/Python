print("*****Stack list Program*****")
list = []
while True:
    print('''
        1 to push elements
        2 to pop elements
        3 to peek elementc
        4 display the list
        5 to exit!!
                ''')   
                
    stack_input = int(input("Enter :- "))
    if stack_input== 1:
        #push element in stack
        
        push_value = input("Enter the value:- ")
        list.append(push_value)
        print(list)

    elif stack_input==2:
        #pop element means the deletion of last element of the stack
        list.pop()
        print(list)

    elif stack_input==3:
        #peeking means printing the last element
        print(f"The last element of the stack is {list[-1]}")

    elif stack_input==4:
        #displaying the list
        print("Displaying the stack!!")
        print(list)

    elif stack_input==5:
        print("Exiting!!")
        break

    else:
        print("Invalid entry!!!")


#queue
'''
Queue in Python
The Queue is a linear data structure.
Stores items in First In First Out (FIFO) manner.
Queue Operations.
Enqueue: Adds an item to the queue.
Dequeue: Removes an item from the queue.
Front: Get the front item from queue.
Rear: Get the last item from queue.'''

