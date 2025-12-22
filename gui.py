from functions import get_todos, write_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo" ,key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=(43, 10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do app",
                   layout=[[label], [input_box, add_button]
                           ,[list_box, edit_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'].strip()

            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo +"\n"
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
window.close()