from functions import get_todos, write_todos
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('',key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo" ,key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do app",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %H:%M:%S"))
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'].strip() + "\n"
            if new_todo == '\n':
                sg.popup("Please add an item first", font=("Helvetica", 10))
                continue
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))
                continue
            new_todo = values['todo'].replace("\n",'')
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 10))
                continue
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
window.close()