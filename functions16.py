FILEPATH=r"C:\Users\MY\PycharmProjects\pythonProject\demo\files\todo.txt"
def get_todos(filepath=FILEPATH):  #default parameter
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w')as file:
        file.writelines(todos_arg)



# print(get_todos())