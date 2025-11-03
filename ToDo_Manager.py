print("*" * 40)
print("Todo Manager Application".center(40))
print("*" * 40)

todos = []
def display_menu():
    print("\nMenu:")
    print("1. View Todos")
    print("2. Add Todo")
    print("3. Remove Todo")
    print("4. Exit")
def view_todos():
    if not todos:
        print("\nNo todos available.")
    else:
        print("\nYour Todos:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
def add_todo():
    todo = input("\nEnter a new todo: ")
    todos.append(todo)
    print(f'Todo "{todo}" added.')
def remove_todo():
    view_todos()
    if todos:
        try:
            idx = int(input("\nEnter the number of the todo to remove: ")) - 1
            if 0 <= idx < len(todos):
                removed = todos.pop(idx)
                print(f'Todo "{removed}" removed.')
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    display_menu()
    choice = input("\nChoose an option (1-4): ")
    if choice == '1':
        view_todos()
    elif choice == '2':
        add_todo()
    elif choice == '3':
        remove_todo()
    elif choice == '4':
        print("Exiting Todo Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


