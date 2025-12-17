from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action= user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        todos = get_todos()

        try:
            number = int(user_action[5:])
            number = number - 1
            todo_to_edit = todos[number]
        except ValueError:
            print("Invalid input! Please enter a valid number")
            continue
        except IndexError:
            print("The index you're trying to access doesn't exist. Try a smaller number.")
            continue

        new_todo = input("Enter a todo: ") + "\n"
        todos[number] = new_todo

        write_todos(todos)

    elif user_action.startswith('complete'):
        todos = get_todos()
            
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos.pop(index).strip("\n")
        except IndexError:
            print("The index you're trying to access doesn't exist. Try a smaller number")
            continue
        except ValueError:
            print("Invalid input! Please enter a valid number")
            continue

        write_todos(todos)

        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")

print("Bye!")