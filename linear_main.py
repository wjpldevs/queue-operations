import sys
from linear_queue import Queue
from customer import Customer

# Project title
print("Queues with customers \n")

# Entry data: Input size
sizeQueue = int(input("Size of queue: "))

# Object creation
customers = [Customer()] * sizeQueue  # Creating an empty static-size queue
queue = Queue()
amountCustomers = 0
running = True

while running:
    # Entry data according menu
    menu = """
    ================ OPERATIONS WITH QUEUES ================
    1. ADD
    2. DELETE
    3. WATCH START
    4. WATCH END
    5. IS EMPTY?
    6. IS FULL?
    7. QUIT
    ========================================================
    """
    print(menu)
    option = int(input("Type your option: "))

    # Define operations
    if option == 1:
        # Get amount of customers to add
        amountCustomers = int(input("How many customers you need to add?: "))
        # Validation 1
        if amountCustomers > len(customers):
            print("Impossible to add more customers!")
        # Validation 2
        if amountCustomers <= 0:
            print("Amount not valid!")
        else:
            for i in range(amountCustomers):
                # Creating customer object
                customerName = input(f"Customer Name: # {i + 1}: ")
                customerEmail = input(f"Cusomter Email: # {i + 1}: ")
                customerAccount = float(input(f"Customer Account: # {i + 1}: "))
                customerObject = Customer(customerName, customerEmail, customerAccount)

                queue.add(customerObject, customers)

            print("\n")

            queue.show(customers)

    elif option == 2:
        # Get amount of customers to delete
        amountCustomers = int(input("How many customers you need to delete?: "))
        # Validation 1
        if amountCustomers > len(customers):
            print("Impossible to add more customers!")
        # Validation 2
        if amountCustomers <= 0:
            print("There is an error!")
        else:
            for i in range(amountCustomers):
                queue.delete(customers)

            print("\n")

            queue.show(customers)

    elif option == 3:  # Show the start of the queue
        start = queue.get_start()
        print(f"The start of the queue is: {start + 1}")

    elif option == 4:  # Show the end of the queue
        end = queue.get_end()
        print(f"The end of the queue is: {end + 1}")

    elif option == 5:  # Show is empty
        if queue.is_empty(customers):
            print("Queue is empty!")
        else:
            print("Queue contains some items or is fully.")

    elif option == 6:  # Show is full
        if queue.is_full(customers):
            print("Queue is full!")
        else:
            print("Queue contains some items or is empty.")

    elif option == 7:  # Quit
        running = False
        sys.exit()

    else:
        print("There is an error in your choose. Check out!")

    answer = input("\n\nDo you want to continue? (y/n):")
    if answer == "y" or answer == "Y":
        running = True
    else:
        running = False
