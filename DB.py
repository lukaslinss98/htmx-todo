import sqlite3
from models.Todo import Todo

TODO_DB_NAME = "todo"
TODO_TABLE_TODOS = "todos"
TODO_FIELD_CONTENT = "content"
TODO_FIELD_STATUS = "status"

def get_todos():
    connection = sqlite3.connect(TODO_DB_NAME)
    cursor = connection.cursor()
    
    rows = cursor.execute(f"SELECT * FROM {TODO_TABLE_TODOS}").fetchall()
    
    connection.close()
    
    return [Todo(row[0], row[1], row[2]) for row in rows]


def insert_todo(input_text):
    connection = sqlite3.connect(TODO_DB_NAME)
    cursor = connection.cursor()
    insert_str = f"INSERT INTO {TODO_TABLE_TODOS} ('{TODO_FIELD_CONTENT}', '{TODO_FIELD_STATUS}') VALUES(?,?)"
    cursor.execute(insert_str, (input_text, 'In Progress'))
    
    connection.commit()
    connection.close()
    