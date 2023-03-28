import streamlit as st
import functions16
todos=functions16.get_todos()

def add_todo():
    to=st.session_state["new_to"] +"\n"
    todos.append(to)
    functions16.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my first app")
st.write("This app is to increase my productivity")

for index,todo in enumerate(todos):
    check=st.checkbox(todo,key=todo)
    if check:
        todos.pop(index)
        functions16.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="Enter a todo:",placeholder="Add a new Todo",on_change=add_todo,key="new_to")


